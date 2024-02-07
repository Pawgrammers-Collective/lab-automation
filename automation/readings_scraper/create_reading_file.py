import os
from rich.console import Console
from automation.main import main

console = Console()

def create_reading_file(title, class_num, questions, readings, videos, bookmarks):
   
    user_directory = os.path.abspath(f'../{os.curdir}')
    console.print("user_directory:", user_directory)
    file_name = f"reading{class_num}.md"
    folder_path = os.path.join(f'{user_directory}/reading_assignments')
    console.print("folder_path:", folder_path)
    file_path = os.path.join(f'{folder_path}/{file_name}')

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    if os.path.exists(file_path):
        console.print("\nThis file already exists.", style="bold red")
        user_input= input("Would you like to overwrite it? (y/n): ")
        
        if user_input == "y":
            console.print("File will be overwritten.", style="bold green")
        
        elif user_input == "n":
            console.print("File not created.", style="bold green")
            main()

        else:
            console.print("Response not recoginized. Returning to main menu.", style="bold red")
            main()

    create_template (title, questions, readings, videos, bookmarks, file_path)


def create_template(title, question_print, readings, videos, bookmarks, file_path):

        # Define the template
    template = f"""
    # {title}

    Description of the assignment

    ## Reading
    {readings}
    
    ## Videos
    {videos}

    ## Bookmark and Review
    {bookmarks}
    
    ## Reading Questions
    {question_print}

    ## Things I want to know more about

    >*Answer*
    """
    # file_path = os.path.join(f'{folder_path}/{file_name}')

    with open(file_path, "w") as file:
        file.write(f"# {template}")
        print('File created successfully!')

    return print (template)





# print(create_reading_file(title, questions))