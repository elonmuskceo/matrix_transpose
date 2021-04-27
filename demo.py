import gradio as gr
import random
import json



EXAMPLE_TTS_EN_MODEL_ID = (
    "julien-c/ljspeech_tts_train_tacotron2_raw_phn_tacotron_g2p_en_no_space_train"
)



def calculator(text: str):
    print(text)
    html = """<div class='audio-slot'></div>
    <script>
    (async () => {
        const c = console;

        const params = {
            method: 'POST',
            body: JSON.stringify({'text': $text}),
            headers: {},
        };
        c.log(params);

        const respFwd = await fetch(
            `https://api-audio-frontend.huggingface.co/models/$model`,
            params
        );

        const blob = await respFwd.blob();
        c.log(blob);

        const audioEl = document.createElement('audio');
        audioEl.src = URL.createObjectURL(blob);
        audioEl.controls = true;
        audioEl.autoplay = true;
        document.querySelector('.audio-slot').appendChild(audioEl);

    })();
    </script>""".replace(
        "$model", EXAMPLE_TTS_EN_MODEL_ID
    ).replace(
        "$text", json.dumps(text),
    )
    return {
        "positive": 0.287,
        "negative": 0.517,
        "neutral": 0.197,
    }, html


iface = gr.Interface(
    calculator, 
    inputs=[
        gr.inputs.Textbox(label="Text-to-Speech", placeholder="Your sentence here...", default="Hello, how are you doing?"),
    ],
    outputs=[
        gr.outputs.Label(label="Text Classification"),
        gr.outputs.HTML(label="Audio"),
    ],
    # examples=[
    #     [5, "add", 3],
    #     [4, "divide", 2],
    #     [-4, "multiply", 2.5],
    #     [0, "subtract", 1.2],
    # ],
    # layout="vertical",
    verbose=True,
    analytics_enabled=False,
    allow_screenshot=False,
    allow_flagging=False,
    # live=True,
)

iface.launch()

print()

