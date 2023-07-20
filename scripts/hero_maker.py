from modules import script_callbacks
from scripts.hm_lib.gui_config import (
    stat_config,
    load_character_attributes

)
from modules.sd_samplers import samplers
from scripts.hm_lib.tools import create_character_string,generate_images
import gradio as gr
import numpy as np
from pathlib import Path

import modules.scripts as scripts
from gradio.outputs import Carousel







def flip_image(x):
    
    return np.fliplr(x)

def get_weight_default():
    return 1

def generate_prompt_and_image(sampler, steps, batch_size, n_iter,*args):
    prompt_string = create_character_string(*args)
    images= generate_images(prompt_string=prompt_string, sampler=sampler,steps=steps,batch_size=batch_size,n_iter=n_iter)
    return prompt_string,images,images

def on_select_base_character(evt: gr.SelectData):  # SelectData is a subclass of EventData
    return f"You selected {evt.value} at {evt.index} from {evt.target}"

def get_select_index(evt: gr.SelectData):
        return evt.index


def on_ui_tabs():
    with gr.Blocks(analytics_enabled=False) as hero_maker:

        gr.Markdown(
            """
            # Character Creator
            """
        )
        
        
        with gr.Tab("Character Description"):
            user_provided_attributes = []
            user_provided_attribute_weights = []
            character_attributes = load_character_attributes(Path(scripts.basedir(),"extensions","hero-maker","data","attributes"))
            
            
            for char_att in character_attributes:
                with gr.Row():
                    user_provided_attributes.append(gr.Dropdown(
                    **char_att.dict(skip_keys=set(["format_string","info"])),
                    ))
                    user_provided_attribute_weights.append(
                        gr.Slider(0, 10,label=char_att.label+" Weight", value=get_weight_default)
                    )   
            
        with gr.Tab("Character Stats"):
            user_stats = {}
            for stat in stat_config:
                user_stats[stat["label"]] = gr.Number(**stat,value=8)
        with gr.Tab("Advanced Settings"):
            sampler = gr.Dropdown(
               [x.name for x in samplers],value = samplers[0].name, interactive=True
            )
            steps = gr.Slider(minimum=1, maximum=150, step=1, label="Sampling Steps", value=20, interactive= True)
            batch_size = gr.Slider(minimum=1, maximum=10, step=1,label="Batch Size", value=1, interactive=True )
            batch_count = gr.Slider(minimum=1,maximum=100, step = 1, label="Batch Count",value = 1,interactive= True)
           
        string_output = gr.Text()
        base_character_images = gr.Gallery(preview=True, variant='panel')
        base_character_state = gr.State()
        selected = gr.Number(show_label=False, placeholder="Selected")

        base_character_images.select(get_select_index,None,selected)
        

        character_button = gr.Button("Create Character")
        character_button.click(
            generate_prompt_and_image, inputs=[
                sampler,
                steps,
                batch_size,
                batch_count,
                *user_provided_attributes,
                *user_provided_attribute_weights
            ],
            outputs= [string_output,base_character_images,base_character_state]


        )
        person_image = gr.Image(source="webcam")
        
        
    statement = gr.Textbox()
        
    return (hero_maker , "Hero Maker", "hero_maker"),
 

script_callbacks.on_ui_tabs(on_ui_tabs)