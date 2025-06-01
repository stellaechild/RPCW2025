import pandas as pd
import re
import os

# Columns to remove
COLUMNS_TO_DROP = [
    "isbn", "rating", "bookFormat", "numRatings", "ratingsByStars",
    "likedPercent", "setting", "coverImg", "bbeScore", "bbeVotes", "price", "language",
    "edition", "publishDate", "description"
]

def clean_authors(author_string):
    if not isinstance(author_string, str):
        return None
        
    # Remove tag Goodreads Author, se existir
    cleaned = re.sub(r'\(Goodreads Author\)', '', author_string, flags=re.IGNORECASE)
    
    # Divide por vírgula, mas respeita parênteses (ex: "Philip Horne (Introduction)")
    parts = re.split(r',\s*(?![^()]*\))', cleaned)
    
    for part in parts:
        part = part.strip()
        if not part:
            continue
        
        # Se tiver parênteses, vê se é um papel relacionado com escrita
        if '(' in part:
            name = re.sub(r'\s*\(.*\)', '', part).strip()
            role_match = re.search(r'\((.*?)\)', part)
            if role_match:
                role = role_match.group(1).lower()
                # Se for papel relacionado com escrita, aceita este como autor
                if any(keyword in role for keyword in ['translator', 'contributor', 'writer', 'introduction']):
                    return part  # Retorna só este
                # Ignora ilustrador, editor, etc.
                elif any(keyword in role for keyword in ['illustrator', 'editor', 'compiler', 'photographer']):
                    continue
                else:
                    return name  # Caso não categorizado, retorna só o nome
        else:
            # Se não tem parênteses, é autor, retorna logo o primeiro
            return part

    # Se nada foi encontrado, retorna None
    return None


def clean_series(series_string):
    """Clean series names by removing volume numbers"""
    return re.sub(r" #\d+", "", str(series_string))

def clean_csv(input_path: str, output_dir: str):
    """
    Process the book dataset:
    1. Load and sample data
    2. Remove unwanted columns
    3. Clean fields
    4. Save cleaned data
    """
    try:
        # Load and sample data
        df = pd.read_csv(input_path).head(500)
        
        # Remove unwanted columns
        df = df.drop(columns=COLUMNS_TO_DROP, errors='ignore')

        # Drop empty rows (except for series)
        cols_to_check = [col for col in df.columns if col != "series"]
        df = df.dropna(subset=cols_to_check)

        # Remove empty awards
        if 'awards' in df.columns:
            df = df[df['awards'].astype(str).str.strip() != '[]']
        
        # Clean fields
        df["series"] = df["series"].apply(clean_series)
        df['author'] = df['author'].apply(clean_authors)
        df = df.drop_duplicates()

        # Ensure output directory exists
        os.makedirs(output_dir, exist_ok=True)
        
        # Save cleaned data
        output_path = os.path.join(output_dir, "new-books.csv")
        df.to_csv(output_path, index=False)
        print(f"Successfully cleaned data saved to:\n{output_path}")
        
        return output_path

    except Exception as e:
        print(f"Error processing file: {e}")
        return None

if __name__ == "__main__":
    input_file = "/home/mirtilo/Quiz_Generator/ontologias/books/books.csv"
    output_dir = "/home/mirtilo/Quiz_Generator/ontologias/books"
    
    cleaned_file = clean_csv(input_file, output_dir)
    
    if cleaned_file:
        # Preview the first 3 rows
        print("\nPreview of cleaned data:")
        print(pd.read_csv(cleaned_file).head(3))
