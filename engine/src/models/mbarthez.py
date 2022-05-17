from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import nltk

class MBARThez:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("/data/mbarthez")
        self.model = AutoModelForSeq2SeqLM.from_pretrained("/data/mbarthez")

    def preprocess(self, text):
        text = text.split(" ")
        text = self.chunks(text, 300)
        if len(text)==1:
            text = text[0]
        encodings =  self.tokenizer(text, return_tensors='pt', padding=True)
        return encodings

    def postprocess_text(preds, labels):
        preds = [pred.strip() for pred in preds]
        preds = ["\n".join(nltk.sent_tokenize(pred)) for pred in preds]

        return preds

    def predict(self, inputs):
        return self.model.generate(inputs['input_ids'], max_length=200)

    def chunks(self, text, n):
        res = []
        for i in range(0, len(text), n):
            res.append(" ".join(text[i:i + n]))
        return res


    def summarize(self, text):
        inputs = self.preprocess(text)
        output = self.predict(inputs)
        output_text = "".join(self.tokenizer.batch_decode(output, skip_special_tokens=True))
        return output_text