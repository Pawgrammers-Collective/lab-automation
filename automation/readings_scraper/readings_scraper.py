from automation.readings_scraper.scrape_elements import get_title, get_questions, get_readings, get_videos, get_bookmarks
# from scrape_elements import get_title, get_questions, get_readings, get_videos, get_bookmarks
from automation.readings_scraper.create_reading_file import create_reading_file


def create_reading_assignment(class_num=33):
    url = f"https://codefellows.github.io/code-401-python-guide/curriculum/class-{class_num}/DISCUSSION"
    title = get_title(url)
    # print("title: ", title)
    questions = get_questions(url)
    readings = get_readings(url)
    videos = get_videos(url)
    bookmarks = get_bookmarks(url)
    # print("bookmarks: ", bookmarks)

    create_reading_file (title, class_num, questions, readings, videos, bookmarks)

    return title, questions, readings, videos, bookmarks

if __name__ == "__main__":
    # title,readings, videos, bookmarks, questions,  = 
    
    create_reading_assignment(33)



    # if title and readings and videos and bookmarks and questions:
    #     template = f"""
    #     # Assignment Title: {title}

    #     ## Questions: 
    #     {questions}

    #     ## Readings:
    #     {readings}

    #     ## Videos:
    #     {videos}

    #     ## Bookmarks:
    #     {bookmarks}
    #     """
    #     print(template)
