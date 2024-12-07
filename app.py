from flask import Flask, render_template, request, flash, redirect, url_for
import pickle
import numpy as np

# Load data
popular_df = pickle.load(open("popular.pkl", "rb"))
pt = pickle.load(open("pt.pkl", "rb"))
books = pickle.load(open("books.pkl", "rb"))
similarity_scores = pickle.load(open("similarity_scores.pkl", "rb"))

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Set a secret key for session management


@app.route("/")
def index():
    return render_template(
        "index.html",
        book_name=list(popular_df["Book-Title"].values),
        author=list(popular_df["Book-Author"].values),
        image=list(popular_df["Image-URL-M"].values),
        votes=list(popular_df["num_ratings"].values),
        rating=list(popular_df["avg_rating"].values),
    )


@app.route("/recommend")
def recommend_ui():
    return render_template("recommend.html")


@app.route("/recommend_books", methods=["post"])
def recommend():
    user_input = request.form.get("user_input")
    try:
        index = np.where(pt.index == user_input)[0][0]

        # Calculate similarity and retrieve similar items
        similar_items = sorted(
            list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True
        )[
            1:11
        ]  # Exclude the first item (the book itself)

        data = []
        for i in similar_items:
            item = []
            temp_df = books[books["Book-Title"] == pt.index[i[0]]]
            item.extend(
                list(temp_df.drop_duplicates("Book-Title")["Book-Title"].values)
            )
            item.extend(
                list(temp_df.drop_duplicates("Book-Title")["Book-Author"].values)
            )
            item.extend(
                list(temp_df.drop_duplicates("Book-Title")["Image-URL-M"].values)
            )

            data.append(item)

        return render_template("recommend.html", data=data)

    except IndexError:
        flash(f"Error: '{user_input}' not found in the dataset.")
        return redirect(url_for("recommend_ui"))  # Redirect back to the recommend page

    except Exception as e:
        flash(f"An unexpected error occurred: {e}")
        return redirect(url_for("recommend_ui"))  # Redirect back to the recommend page


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
