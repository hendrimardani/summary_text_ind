import keras
import argparse
from transformers import pipeline
from transformers import AutoTokenizer
from transformers import TFAutoModelForSeq2SeqLM, DataCollatorForSeq2Seq


if __name__ == "__main__":
    MODEL_CHECKPOINT = "t5-small"
    LEARNING_RATE = 1e-7
    MIN_TARGET_LENGTH = 5
    MAX_TARGET_LENGTH = 256

    def build_model():
        if MODEL_CHECKPOINT in ["t5-small", "t5-base", "t5-large", "t5-3b", "t5-11b"]:
            prefix = "summarize: "
        else:
            prefix = ""

        model = TFAutoModelForSeq2SeqLM.from_pretrained(MODEL_CHECKPOINT)
        optimizer = keras.optimizers.Adam(learning_rate=LEARNING_RATE)
        model.compile(optimizer=optimizer)
        return model
        
    try:
        parser = argparse.ArgumentParser(description="Model has been trained by Hendri Mardani")
        parser.add_argument('-f', '--file', type=str, required=True, help="Upload file yang mau di simpulkan berdasarkan lokasinya ektensi:[.txt]")
        parser.add_argument('-m', '--model', type=str, required=True, help="Upload model pre-trained sesuai dengan lokasinya")
        args = parser.parse_args()

        lokasi_model = args.model
        model = build_model()
        model.load_weights(lokasi_model)

        # kalimat_prediksi = "Penggunaan plastik yang semakin marak menjadi masalah lingkungan yang tidak kunjung usai. Plastik adalah bahan anorganik yang tidak ramah lingkungan. Hal ini disebabkan sifat plastik yang tidak mudah hancur dan terurai oleh tanah. Butuh waktu beratus-ratus tahun hingga plastik terurai dalam tanah."
        tokenizer = AutoTokenizer.from_pretrained(MODEL_CHECKPOINT)
        summarizer = pipeline("summarization", model=model, tokenizer=tokenizer, framework="tf")

        if args.file:
            with open(args.file) as f:
                kalimat_prediksi = f.read()

        summarizer = summarizer(
            kalimat_prediksi,
            min_length=MIN_TARGET_LENGTH,
            max_length=MAX_TARGET_LENGTH,
        )
        print()
        print("==="*40)
        print("Isi kalimatnya : ", kalimat_prediksi)
        print()
        print("Ringkasan Teks : ", summarizer[0]["summary_text"])
    except:
        print()
        print("Wajib pakai argument --file dan --model sesuai dengan Lokasi File!!!, ketik --help untuk bantuan")
