[![AUP](https://img.shields.io/badge/Acceptable%20Use%20Policy-Read%20Now-blue)](./ACCEPTABLE_USE_POLICY.md)

# Hero Maker
Just a fun proof of concept automatic1111 plugin for guided prompt generation and face swapping. 

Focused around creating a guided prompt based on D&D terms used in character creation.

## Installation
1. Use automatic1111's "Install from ULR tab"
2. In the install directory for the plugin (typically under extensions/hero-maker) create a models folder and add [this](https://huggingface.co/deepinsight/inswapper/blob/main/inswapper_128.onnx) model with the name "inswapper_128.onnx"



## Notes
- Quality of image is completely driven by the stable diffusion checkpoint being used. 
- Requires webcam


## TODO

- [ ] Implement sfw filter for checking images before faceswap
- [ ] Toggle for sfw slider for adjusting the filter
- [ ] Improve UX
- [ ] Add ability to switch between webcam and existing images
- [ ] Test different models and document performance/utility for different character settings
- [ ] Implement stats influence the prompt



## Acceptable Use Policy

Please read and adhere to our [Acceptable Use Policy](./ACCEPTABLE_USE_POLICY.md) before using this plugin. By using the plugin, you agree to comply with the guidelines outlined in the policy.

