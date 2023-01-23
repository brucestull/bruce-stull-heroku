# Project Directory Structure

* `tree /f /a`:  

    ```console
    PS C:\Users\FlynntKnapp\Programming\bruce-stull> tree /f /a .
    Folder PATH listing for volume Windows
    Volume serial number is 54A3-AA4E
    C:\USERS\FLYNNTKNAPP\PROGRAMMING\BRUCE-STULL
    |   .gitignore
    |   db.sqlite3
    |   LICENSE
    |   manage.py
    |   Pipfile
    |   Pipfile.lock
    |   Procfile
    |   README.md
    |
    +---.vscode
    |       html.code-snippets
    |       launch.json
    |
    +---accounts
    |   |   admin.py
    |   |   apps.py
    |   |   forms.py
    |   |   models.py
    |   |   tests.py
    |   |   urls.py
    |   |   views.py
    |   |   __init__.py
    |   |
    |   \---migrations
    |           0001_initial.py
    |           __init__.py
    |
    +---blog
    |   |   admin.py
    |   |   apps.py
    |   |   forms.py
    |   |   models.py
    |   |   tests.py
    |   |   urls.py
    |   |   views.py
    |   |   __init__.py
    |   |
    |   +---migrations
    |   |       __init__.py
    |   |
    |   \---templates
    |       \---blog
    |               blog_category.html
    |               blog_detail.html
    |               blog_index.html
    |
    +---config
    |   |   asgi.py
    |   |   urls.py
    |   |   wsgi.py
    |   |   __init__.py
    |   |
    |   \---settings
    |           common.py
    |           development.py
    |           production.py
    |
    +---notes
    |       00_commands_and_links.md
    |       00_directory_structure.md
    |       00_notes.md
    |
    +---projects
    |   |   admin.py
    |   |   apps.py
    |   |   models.py
    |   |   tests.py
    |   |   urls.py
    |   |   views.py
    |   |   __init__.py
    |   |
    |   +---migrations
    |   |       __init__.py
    |   |
    |   \---templates
    |       \---projects
    |               project.html
    |               projects.html
    |
    +---templates
    |   |   base.html
    |   |   home.html
    |   |   staff.html
    |   |   user.html
    |   |
    |   \---registration
    |           login.html
    |           password_reset_complete.html
    |           password_reset_confirm.html
    |           password_reset_done.html
    |           password_reset_form.html
    |           signup.html
    |           update.html
    |
    \---test_images
            test_image_01.png
            test_image_02.png
            test_image_03.png

    PS C:\Users\FlynntKnapp\Programming\bruce-stull>
    ```

## Repository Links

[README.md](../README.md)
