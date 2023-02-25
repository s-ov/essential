class Editor:
    LICENSE_KEY = 'qwerty123456'

    def view_document(self):
        return 'Document is empty.'

    def edit_document(self):
        return "Option 'edit' is not available for free version."


class ProEditor(Editor):
    def edit_document(self):
        return 'You can edit this document.'


license_key = input('Enter the license key to get access to edit the document: ')
if license_key == Editor.LICENSE_KEY:
    editor = ProEditor()
else:
    editor = Editor()
print(editor.view_document())
print(editor.edit_document())
