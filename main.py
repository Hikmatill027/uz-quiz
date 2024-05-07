import turtle
import pandas as pd
ALIGN = 'center'
FONT = ("Arial", 18, 'normal')

screen = turtle.Screen()
screen.title("Uzbekistan Quiz")
screen.setup(width=1100, height=800)
image = "Uzbekistan_regions.gif"
screen.addshape(image)
turtle.shape(image)

all_regions_data = pd.read_csv("uz_regions.csv")
all_regions = all_regions_data["regions"].to_list()
chosen_regions = []
unanswered_regions = []

while len(chosen_regions) < 13:
    user_answer = screen.textinput(title=f"{len(chosen_regions)}/12 Regions",
                                   prompt="What regions do you know?").capitalize()
    if user_answer == "Quit":
        break
    if user_answer in all_regions:
        region_coordinate = all_regions_data[all_regions_data["regions"] == user_answer]
        chosen_regions.append(user_answer)
        x = region_coordinate["x"].astype(int)
        y = region_coordinate["y"].astype(int)

        t = turtle.Turtle()
        t.hideturtle()
        t.pu()
        t.goto(int(x), int(y))
        t.color("green")
        t.write(user_answer, align=ALIGN, font=FONT)
    unanswered_regions = [region for region in all_regions if region not in chosen_regions]
    non_regions_df = pd.DataFrame(unanswered_regions)
    non_regions_df.to_csv("unanswered_regions.csv")
screen.exitonclick()
