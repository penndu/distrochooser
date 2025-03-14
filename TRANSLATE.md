# How to translate

The application stores all translation inside of *.json files inside of the first path defined within the `settings.py`
`LOCALES_PATH`.

All files follow the format `<scope>-<iso-639-3>.json`. Translations can be updated using the JSON files or can be
updated during runtime.

## Inline translate

The app features a button, labelled with "help translation". This button triggers the mode to be able to change
any translatable value within the application. If the data ist stored, the user session will continue use this proposal.

This approach aims to replace the need for third-party tools and services.

## Persist proposals

To persist proposals, the backend CLI interface can be used. the command `python manage.py language` is to be used here with following commands:

-`python manage.py language en` - List all proposals for lang code `en`
- `python manage.py language en --clear` - Delete all proposals
- `python manage.py language en --delete <id>` - Delete a given proposal by it's id
- `python manage.py language en --approve <id>` - Approve given proposals (ID's will be printed on screen by the list command)
- `python manage.py language en --persist` - All approved proposals will be written into files. If the language key is present within the json files, the file will be updated (first hit counts). If not, a file `additional-<langcode>.json` will be read 

> Please note that changes on the json files require a restart