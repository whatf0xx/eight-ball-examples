from pickle import dump
from eight_ball.ball import Ball
from eight_ball.simulation import Simulation
import matplotlib.pyplot as plt

if __name__ == "__main__":
    sim = Simulation(1.0)
    balls = [Ball(
                 pos=(-0.6+(i%40)*0.03, -0.6+(i//40)*0.03),
                 vel=(4 if i == 0 else 0, 3 if i == 0 else 0),
                 r=0.001)
            for i in range(1600)]
    sim.add_balls(balls)
    sim.initialise()
    # sim.comic_strip(4)
    for _ in range(100_000):
        sim.next_collision()
    times_dist = sim.collision_times(1_000_000, 0., 0.02, 600)
    with open("data/low_density_collision_times.pkl", "wb+") as f:
        dump(times_dist, f)
    fig = plt.figure()
    ax = plt.axes()
    ax.bar(times_dist["centres"], times_dist["counts"], times_dist["width"])
    plt.show()
