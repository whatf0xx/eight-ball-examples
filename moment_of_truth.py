from pickle import dump
from eight_ball.ball import Ball
from eight_ball.simulation import Simulation
import matplotlib.pyplot as plt

if __name__ == "__main__":
    sim = Simulation(1.0)
    _balls = [Ball(
                   pos=(0.2+(i%2)*0.3, 0.2+(i//2)*0.3),
                   vel=(.4 if i == 0 else 0, .3 if i == 0 else 0),
                   r=0.05)
        for i in range(4)]
    sim.add_balls(_balls)
    sim.initialise()
    for _ in range(0, 2_115_609):
        sim.next_collision()

    fig = sim.comic_strip(4)
    # fig.supxlabel("Position (m)")
    # fig.supylabel("Position (m)")
    plt.savefig("figs/moment_of_truth.png", dpi=300)
