# Teo Patrosio: CS163 Final Project - Least Median of Squares 
Fall 2021

# About
- [Presentation Slides](https://docs.google.com/presentation/d/1vKthO3TACfFR4HHBpg1w-rvgK-I4t2imMGqZsZWwH3U/edit?usp=sharing)
- [Github Repo](https://github.com/imnotartsy/cs163)


# Installation: Manim
[Library](https://github.com/3b1b/manim)

There are instructions to get manim working on a variety of operating systems
on the manim page linked above. I did not develop directly on halligan because
of the need for consistent access to a display.

I personally use the Anaconda install:
> ## Anaconda Install
> Install LaTeX as above.

> Create a conda environment using ```conda create -n manim python=3.8```.

> Activate the environment using ```conda activate manim```.

> Install manimgl using ```pip install -e .```.


# Running my Project
- After installing manim, there are two main commands I like to run:
  - ```manimgl manim_test2.py Naive -o``` --> -o to write the scene to a file and open the result
  - ```manimgl manim_test2.py Naive -so``` --> -so to skip to the end and just show the final frame.
- Various parameters such as the coordinate space and also point count can be editted at the top of the class definition.


# What I Learned
## Takeaways
- Animations are pretty difficult! Python has been installed strangely on my laptop for the last few months as fundamental libraries were updated for ARM architectures. I had initially started using manim on Google Colab, using manim community however that somehow broke between Thanksgiving and Finals, causing me to start again.
- Runtime matters, especially when it determines render time. I chose a naive algorithm, which was inherently exceptionally slow. I wanted to spend time on the animation and showing steps and really working through the atomic geometric problems.
- A lot of fundamental geometry/algebra steps are really abstracted out with algorithms. I think I'll cover this better in my presentation, but it's been a Hot minute since I've found the distance between two parallel lines and automating it was interesting.


## Testing
- Always have as much output as possible as with all programming! 
