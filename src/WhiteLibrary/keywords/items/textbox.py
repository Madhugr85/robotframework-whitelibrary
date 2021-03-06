from TestStack.White.UIItems import TextBox
from WhiteLibrary.keywords.librarycomponent import LibraryComponent
from WhiteLibrary.keywords.robotlibcore import keyword


class TextBoxKeywords(LibraryComponent):
    @keyword
    def input_text_to_textbox(self, locator, input_value):
        """
        Writes text to a textbox.

        ``locator`` is the locator of the text box.

        ``input_value`` is the text to write.
        """
        textBox = self.state._get_typed_item_by_locator(TextBox, locator)
        textBox.Text = input_value

    @keyword
    def verify_text_in_textbox(self, locator, expected):
        """
        Verifies text in a text box.

        ``locator`` is the locator of the text box.

        ``expected`` is the expected text of the text box.
        """
        textbox = self.state._get_typed_item_by_locator(TextBox, locator)
        self.state._verify_value(expected, textbox.Text)

    @keyword
    def get_text_from_textbox(self, locator):
        """
        Gets text from text box.

        ``locator`` is the locator of the text box.

        """
        textbox = self.state._get_typed_item_by_locator(TextBox, locator)
        return textbox.Text
