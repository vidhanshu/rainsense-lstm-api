import random

# Tips for when the model predicts 1 (there will be rain)
tips_1 = [
    "Practise rainwater harvesting to reduce the wastage of rainwater and store it for future use. Rainwater harvesting is the process of collecting and storing rainwater from rooftops, catchments, or other sources. It can be used for domestic, agricultural, or environmental purposes.",
    "Install a rain sensor, a soil moisture sensor or a smart irrigation controller as part of your automated sprinkling system to reduce over-watering. These devices can sense the amount of rainfall and soil moisture and adjust the watering schedule accordingly.",
    "Use mulch around your plants to retain soil moisture and prevent erosion. Mulch is any material that covers the soil surface, such as straw, leaves, wood chips, or compost. It can also suppress weeds and improve soil quality.",
    "Avoid using pesticides and fertilizers that can contaminate the runoff water and harm the aquatic life. Instead, use organic or natural alternatives that are safer for the environment.",
    "Create small reservoirs and percolation tanks to hold run-off water and recharge the groundwater. These structures can also moderate the flood peaks at downstream areas and prevent soil erosion.",
    "Collect rainwater in barrels or tanks and use it for gardening, washing, or flushing toilets. This will reduce your dependence on municipal water supply and save money.",
    "Install a rain garden or a bioswale in your yard to capture and filter stormwater runoff. This will prevent flooding, erosion, and pollution of nearby water bodies.",
    "Check your roof, gutters, and pipes for leaks and repair them before the rainy season. This will prevent water wastage and damage to your property.",
    "Avoid using pesticides, fertilizers, and other chemicals on your lawn or garden before it rains. These substances can wash off into storm drains and contaminate water sources. Use organic or natural alternatives instead.",
    "Reduce your water consumption during rainy days by taking shorter showers, turning off the faucet when not in use, and using water-efficient appliances. This will help conserve water for dry periods and reduce the pressure on water treatment plants."
]

# Tips for when the model predicts 0 (there won't be rain)
tips_0 = [
    "Install flow-restricting shower heads to save water during showers. These devices reduce the amount of water that flows out of the shower head, thus saving water and energy.",
    "Take bucket-baths instead of showers. Bucket-baths use less water than showers, as they require only a fixed amount of water to fill the bucket. Showers, on the other hand, can use up to 10 times more water than bucket-baths.",
    "Turn off the tap while shaving or brushing teeth. This simple habit can save a lot of water that would otherwise go down the drain. A running tap can waste up to 6 litres of water per minute.",
    "Immediately fix any leaking taps and pipes in your homes. Leaking taps and pipes can waste a lot of water over time and increase your water bills. A dripping tap can waste up to 15 litres of water per day.",
    "Use grey water recycling systems to reuse the wastewater from sinks, showers, washing machines, etc. for non-potable purposes such as flushing toilets, watering plants, or cleaning floors. Grey water recycling can reduce your freshwater consumption by up to 50%.",
    "Mulch your plants and trees to retain soil moisture and reduce evaporation. This will help them survive drought conditions and reduce the need for watering.",
    "Use drip irrigation or sprinklers with timers and sensors to water your plants efficiently and avoid overwatering. This will save water and prevent runoff and soil erosion.",
    "Reuse greywater from sinks, showers, and washing machines for watering plants, flushing toilets, or cleaning floors. This will reduce your water demand and wastewater generation.",
    "Install low-flow showerheads, faucets, and toilets to reduce your water usage in the bathroom. This will save water and money on your water bills.",
    "Practice xeriscaping or landscaping with drought-tolerant plants that require less water and maintenance. This will enhance the beauty of your yard and attract wildlife."
]


def get_tip(prediction):
    # prediction is either 0 or 1
    if prediction == 0:
        # choose a random tip from tips_0 array
        tip = random.choice(tips_0)
    elif prediction == 1:
        # choose a random tip from tips_1 array
        tip = random.choice(tips_1)
    else:
        # invalid prediction
        tip = "Please enter either 0 or 1 as the prediction."
    
    return tip