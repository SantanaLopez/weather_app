function Books(title, author, pages, read)
{
    this.title = title;
    this.author = author;
    this.pages = pages;
    this.read = read;
    this.sayBooks = function(){
        console.log(this.title + " by " + this.author + ", " + this.pages + " pages, " +
            this.read + "."
        )
     } 
}

const books = new Books('The Hobbit', 'J.R.R. Tolkien', 295, "not read yet")
books.sayBooks();