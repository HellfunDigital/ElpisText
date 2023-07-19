```python
import random

class PlotGenerator:
    def __init__(self):
        self.plot_elements = ["Introduction", "Rising Action", "Climax", "Falling Action", "Resolution"]
        self.plot_structure = []

    def generate_plot(self):
        random.shuffle(self.plot_elements)
        self.plot_structure = self.plot_elements
        return self.plot_structure

if __name__ == "__main__":
    plot_generator = PlotGenerator()
    print(plot_generator.generate_plot())
```