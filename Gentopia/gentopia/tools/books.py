from typing import AnyStr, List, Optional, Type, Any
from gentopia.tools.basetool import BaseTool, BaseModel, Field
from pydantic import BaseModel, Field


#Recommend Books by Genre
class RecommendBooksByGenreArgs(BaseModel):
    genre: str

class RecommendBooksByGenre(BaseTool):
    name = "recommend_books_by_genre"
    description = "Recommend books based on a specific genre"
    args_schema: Optional[Type[BaseModel]] = RecommendBooksByGenreArgs

    def _run(self, genre: str) -> str:
        # Construct the prompt for OpenAI API
        prompt = (
            f"Can you suggest books that fall under the {genre} category? "
            f"Please include the title, author, and a summary of the book's exploration of that topic."
        )
        return prompt

    async def _arun(self, genre: str) -> str:
        """
        Asynchronous version of the book recommendation search.
        """
        return self._run(genre)


#  Recommend Books by Author
class RecommendBooksByAuthorArgs(BaseModel):
    author: str = Field(description="Author of books to recommend")


class RecommendBooksByAuthor(BaseTool):
    name = "recommend_books_by_author"
    description = "Recommend books based on a specific author"
    args_schema: Optional[Type[BaseModel]] = RecommendBooksByAuthorArgs

    def _run(self, author: str) -> str:
        # Construct the prompt for OpenAI API
        prompt = (
            f"Can you recommend books written by {author}? "
            f"Please include the title, author, and a summary of the book's exploration of that topic."
        )
        return prompt

    async def _arun(self, author: AnyStr) -> str:
        return self._run(author)


# Recommend Books by Topic
class RecommendBooksByTopicArgs(BaseModel):
    topic: str 


class RecommendBooksByTopic(BaseTool):
    name = "recommend_books_by_topic"
    description = "Recommend books based on a specific topic"
    args_schema: Optional[Type[BaseModel]] = RecommendBooksByTopicArgs

    def _run(self, topic: str) -> str:
        # Construct the prompt for OpenAI API
        prompt = (
            f"Can you recommend books that focus on the topic of {topic}."
            f"Please include the title, author, and a summary of the book's exploration of that topic."
        )
        return prompt

    async def _arun(self, topic: AnyStr) -> str:
        return self._run(topic)


# Find Similar Books
class RecommendSimilarBooksArgs(BaseModel):
    title: str = Field(description="Find books similar to this title")


class RecommendSimilarBooks(BaseTool):
    name = "find_similar_books"
    description = "Recommend books that are similar to a given book"
    args_schema: Optional[Type[BaseModel]] = RecommendSimilarBooksArgs

    def _run(self, title: str) -> str:
       # Construct the prompt for OpenAI API
        prompt = (
            f"Can you recommend books similar to '{title}' that share the same genre, explore similar themes "
            f"Provide the title, author, and a brief description for each book."
        )
        return prompt

    async def _arun(self, title: AnyStr) -> str:
        return self._run(title)



# Recommend Trending Books
class RecommendTrendingBooksArgs(BaseModel):
    genre: str = Field(..., description="Genre to find trending books for.")
    max_results: int = Field(5, description="Maximum number of trending books to return.")

class RecommendTrendingBooks(BaseTool):
    name = "recommend_trending_books"
    description = "Recommend trending books based on genre"
    args_schema: Type[BaseModel] = RecommendTrendingBooksArgs

    def _run(self, genre: str, max_results: int = 5) -> str:
        # Construct the prompt for OpenAI API
        prompt = (
            f"Can you suggest me {max_results} trending books in the genre '{genre}'. "
            f"Provide the title, author, and a brief description for each book."
        )
        return prompt
    
    async def _arun(self, genre: str, max_results: int) -> str:
        return self._run(genre, max_results)




if __name__ == "__main__":
    agent = RecommendBooksByGenre()
    ans = agent._run(genre="science fiction")
    print(ans)
