from transformers import CamembertTokenizer, EncoderDecoderModel

class Camembert:
    def __init__(self):
        self.tokenizer = CamembertTokenizer.from_pretrained("/data/camembert")
        self.model = EncoderDecoderModel.from_pretrained("/data/camembert")

    def generate_summary(self, string):
        # Tokenizer will automatically set [BOS] <text> [EOS]
        inputs = self.tokenizer(string, padding="max_length", truncation=True, max_length=512, return_tensors="pt")
        input_ids = inputs.input_ids
        attention_mask = inputs.attention_mask
        outputs = self.model.generate(input_ids, attention_mask=attention_mask)
        # all special tokens including will be removed
        output_str = self.tokenizer.batch_decode(outputs, skip_special_tokens=True)

        return output_str
    
    def post_process(self, text, summary):
            
        article_splitted = text.split(".")
        article_cleaned = []

        for data in article_splitted:
            data_cleaned = data.replace("\n", " ")
            article_cleaned.append(data_cleaned)

        #Convert list to a string
        raw_data = "".join(summary)

        # Split the string into sentences
        raw_data_splitted = raw_data.split(".")

        #Select the last element
        last_sentence = raw_data_splitted[-1]

        #Count the number of words the last sentence
        word_list_last_sentence = last_sentence.split()
        number_of_words = len(word_list_last_sentence)

        """
        If the number of the last sentence is >=5 words we add the last cutting sentence to the sammary
        Otherwise the last cutting sentence is removed from the summary
        """

        if number_of_words >= 5:
            for data in article_cleaned:
                if last_sentence[:10] in data[:10]:
                    raw_data_splitted.pop()
                    raw_data_splitted.append(data)
                    summary_formatting = []
                    #Build the new summary
                    for data in raw_data_splitted:
                        sentence = data+"."
                        summary_formatting.append(sentence)
                    summary_cleaned = ''.join(summary_formatting)
                    return summary_cleaned
        else:
            #Remove the last sentence
            raw_data_splitted.pop()

            #Build the new summary
            summary_cleaned = '.'.join(raw_data_splitted)
            summary_cleaned = summary_cleaned+'.'
            return summary_cleaned

    def summarize(self, text):
        summary_raw = self.generate_summary(text)
        return self.post_process(text, summary_raw)