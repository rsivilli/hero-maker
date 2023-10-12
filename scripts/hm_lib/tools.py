import json
import os

import cv2
import insightface
import modules.shared as shared
import numpy as np
from modules import processing, sd_samplers
from modules.shared import cmd_opts, opts
from PIL import Image

import scripts.hm_lib.gui_config as attr_config
from scripts.hm_lib.logger import logger
from scripts.hm_lib.stat_config import stat_config


def stat_lookup(stat: str, value: int) -> str | None:
    stat_values = stat_config.get(stat)
    if stat_values is None:
        raise KeyError(f"There is no configuration for stat {stat}")

    for stat_desc in stat_values:
        if value >= stat_desc.min_value and value <= stat_desc.max_value:
            return stat_desc.desc
        raise ValueError(
            f"For the stat {stat}, there is no description for value {value}"
        )


def create_character_string(*args) -> str:
    prompt = []
    arg_length = len(args)
    if arg_length % 2 != 0:
        raise ValueError(
            "The number of arguments should be divisible by two if correctly coupling attributes and weights. This is not the case currently"
        )
    for i in range(int(arg_length / 2)):
        choices = attr_config.attribute_list[i].choices
        format_string = attr_config.attribute_list[i].format_string
        weight = args[int(arg_length / 2) + i]
        if args[i] == "" or args[i] is None:
            continue
        if isinstance(choices, list):
            if format_string is None:
                prompt.append(args[i])
            else:
                prompt.append(format_string.format(args[i], weight))
        elif isinstance(choices, dict):
            if format_string is None:
                prompt.append(choices.get(args[i]) or args[i])
            else:
                prompt.append(
                    format_string.format(choices.get(args[i]) or args[i], weight)
                )

    # prompt.append(f"A portat of a {user_gender} {race} {user_class} in a {setting} setting")
    prompt.extend(["extreme detail", "8k", "modelshoot style"])
    prompt_string = ",".join([p for p in prompt if p != "" and p is not None])
    return prompt_string


def generate_images(
    prompt_string: str,
    sampler: str,
    steps: int,
    batch_size: int,
    n_iter: int,
):
    p = processing.StableDiffusionProcessingTxt2Img(
        sd_model=shared.sd_model,
        outpath_samples=opts.outdir_samples or opts.outdir_txt2img_samples,
        outpath_grids=opts.outdir_grids or opts.outdir_txt2img_grids,
        prompt=prompt_string,
        # styles=prompt_styles,
        negative_prompt="""
        nude, (bad art, low detail, pencil drawing:1.4), (plain background, grainy, low quality, 
        mutated hands and fingers:1.4), (watermark, thin lines:1.2), (deformed, signature:1.2), (blurry, ugly, bad anatomy, 
        extra limbs, undersaturated, low resolution), disfigured, deformations, out of frame, amputee, bad proportions, 
        extra limb, missing limbs, distortion, floating limbs, out of frame, poorly drawn face, poorly drawn hands, text, malformed, missing fingers, cropped
        """,
        # seed=seed,
        sampler_name=sampler,
        batch_size=batch_size,
        n_iter=n_iter,
        steps=steps,
        # cfg_scale=cfg_scale,
        width=512,
        height=512,
        # restore_faces=restore_faces,
        # tiling=tiling,
        # enable_hr=enable_hr,
        # denoising_strength=denoising_strength if enable_hr else None,
        # hr_scale=hr_scale,
        # hr_upscaler=hr_upscaler,
        # hr_second_pass_steps=hr_second_pass_steps,
        # hr_resize_x=hr_resize_x,
        # hr_resize_y=hr_resize_y,
        # hr_sampler_name=sd_samplers.samplers_for_img2img[hr_sampler_index - 1].name if hr_sampler_index != 0 else None,
        # hr_prompt=hr_prompt,
        # hr_negative_prompt=hr_negative_prompt,
        # override_settings=override_settings,
    )
    processed = processing.process_images(p)
    p.close()
    shared.total_tqdm.clear()
    print(processed)

    return processed.images
