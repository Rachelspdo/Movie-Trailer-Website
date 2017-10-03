import media  # import media that we create Class
import fresh_tomatoes
wonder_women = media.Movie(
                        "Wonder Women",
                        "Before she was Wonder Woman, she was Diana...",
                        "http://bit.ly/2yjJswr",
                        "https://www.youtube.com/watch?v=VSB4wGIdDwo"
                        )

independent_day = media.Movie(
                            "Independent Day",
                            "The aliens are coming and invading Earth...",
                            "http://bit.ly/2xbSXZz",
                            "https://www.youtube.com/watch?v=O3a0kv1sJxg"
                            )

hidden_figures = media.Movie(
                            "Hidden Figures",
                            "Three brilliant African-American women at NASA..",
                            "http://bit.ly/2kAjOIz",
                            "https://www.youtube.com/watch?v=q8FZCYtyxQk"
                            )

spider_man = media.Movie(
                        "Spider-Man: Homecoming",
                        "Peter Parker tries to balance his life with his...",
                        "http://bit.ly/2wtKfpX",
                        "https://www.youtube.com/watch?v=U0D3AOldjMU"
                        )

meters_down = media.Movie(
                        "47 Meters Down",
                        "Kate and Lisa go diving in shark-infested waters...",
                        "http://bit.ly/2xVOTAF",
                        "https://www.youtube.com/watch?v=iKjvse77vjU"
                        )

lost_city = media.Movie(
                        "The Lost City of Z",
                        "British explorer Percy Fawcett journeys into the...",
                        "http://bit.ly/2fKBa9c",
                        "https://www.youtube.com/watch?v=S0eY-7uYcCU"
                        )

# wonder_women.show_trailer()
movies = [
    wonder_women, independent_day, hidden_figures,
    spider_man, meters_down, lost_city]
fresh_tomatoes.open_movies_page(movies)
