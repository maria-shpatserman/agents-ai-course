import gradio as gr
from worker import Sidekick


async def setup():
    sidekick = Sidekick()
    await sidekick.setup()
    return sidekick


async def process_message(sidekick, message, history):
    results = await sidekick.run_superstep(message, history)
    return results, sidekick




with gr.Blocks(title="My Helper", theme=gr.themes.Default(primary_hue="emerald")) as ui:
    gr.Markdown("## Test Helper Personal Co-Worker")
    sidekick = gr.State()

    with gr.Row():
        chatbot = gr.Chatbot(label="Helper", height=300, type="messages")
    with gr.Row():
        message = gr.Textbox(show_label=False, placeholder="Your request to the Sidekick")
       
    with gr.Row():
        go_button = gr.Button("Go!", variant="primary")

    ui.load(setup, [], [sidekick])
    message.submit(
        process_message, [sidekick, message, chatbot], [chatbot, sidekick]
    )
   
    go_button.click(
        process_message, [sidekick, message, chatbot], [chatbot, sidekick]
    )
   

ui.launch(inbrowser=True)
