import pandas as pd

def get_user_reviews_book_data(user_id, ratings_file, books_file):
    # Load CSV files into dataframes
    ratings_df = pd.read_csv(ratings_file)
    books_df = pd.read_csv(books_file)

    # Filter reviews for the specified user
    user_reviews = ratings_df[ratings_df['UserID'] == user_id]

    # Extract titles from the user reviews
    review_titles = user_reviews['Title'].unique()

    # Filter books dataframe to get full records for matching titles
    book_data = books_df[books_df['Title'].isin(review_titles)]

    # Merge the user reviews with the book data to add the rating field
    merged_data = book_data.merge(user_reviews[['Title', 'UserReviewScore']], on='Title')

    # Drop the first column
    merged_data_dropped = merged_data.iloc[:, 1:]

    # Convert to a multi-dimensional array 
    book_data_array = merged_data_dropped.values.tolist()

    return book_data_array

def get_user_reviews_book_dataAPI(user_id, ratings_array, books_file):
    # Convert ratings array to dataframe
    ratings_df = pd.DataFrame(ratings_array, columns=['UserID', 'Title', 'UserReviewScore'])
    
    # Load books file into dataframe
    books_df = pd.read_csv(books_file)

    # Filter reviews for the specified user
    user_reviews = ratings_df[ratings_df['UserID'] == user_id]

    # Extract titles from the user reviews
    review_titles = user_reviews['Title'].unique()

    # Filter books dataframe to get full records for matching titles
    book_data = books_df[books_df['Title'].isin(review_titles)]

    # Merge the user reviews with the book data to add the rating field
    merged_data = book_data.merge(user_reviews[['Title', 'UserReviewScore']], on='Title')

    # Drop the first column
    merged_data_dropped = merged_data.iloc[:, 1:]
    
    # Convert to a multi-dimensional array 
    book_data_array = merged_data_dropped.values.tolist()

    # Print the book data array
    print(book_data_array)

    return book_data_array


# # Usage example
# user_id = 'A3M174IC0VXOS2'  # Replace with the actual UserID
# ratings_file = '../datasets/ratings.csv'
# books_file = '../datasets/author_publisher_label_encoded_books.csv'

# book_data_array = get_user_reviews_book_data(user_id, ratings_file, books_file)
# print(book_data_array)

# Example usage:
ratings_array = [
    ['A3M174IC0VXOS2', 'The Alchemist', 4.5],
    ['A3M174IC0VXOS2', 'Unbroken', 3.0],
    ['A1B2C3D4E5F6G7', 'Watchmen', 5.0]
]

books_file = '../datasets/author_publisher_label_encoded_books.csv'

get_user_reviews_book_dataAPI('A3M174IC0VXOS2', ratings_array, books_file)