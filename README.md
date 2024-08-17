# Parametric Function Demonstration Program

A Python program that demonstrates how to compute parametric functions given two turning points.
- In the current version of this test program, the following parametric functions are computed.
  -  Sine function of the form, $f(t) = a \cdot \sin(w \cdot (t - p)) + c$, given two turning points. 
  -  Cubic polynomial of the form, $f(x) = a \cdot x^3 + b \cdot x^2 + c \cdot x + d$, given two turing points.
- The program also shows how to find solutions for the coefficients of a cubic polynomial, given two turning points.

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Features](#features)
4. [Contributing](#contributing)
5. [License](#license)
6. [Contact Information](#contact-information)
7. [Acknowledgements](#acknowledgements)

## Installation

### Prerequisites

- Python 3.x

### Steps

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/your-repo.git
    ```

2. Navigate to the project directory:
    ```sh
    cd your-repo
    ```

3. Create and activate the virtual environment using the provided batch files:
    - To create the virtual environment and activate it, run:
      ```sh
      venv_create.bat
      ```
    - If you need to activate the virtual environment later, run:
      ```sh
      venv_activate.bat
      ```
    - To deactivate the virtual environment, run:
      ```sh
      venv_deactivate.bat
      ```
    - To delete the virtual environment, run:
      ```sh
      venv_delete.bat
      ```

4. Install the required packages:
    ```sh
    venv_install_requirements.bat
    ```

5. To save the current list of installed packages to `venv_requirements.txt`, run:
    ```sh
    venv_save_requirements.bat
    ```

## Usage

### Parametric Functions

The functions `cubic_segment` and `sin_segment` are the parametric functions demonstrated in this program.

Both functions take two input vector parameters that serve as the parametric points through which the functions pass. 
- Parameters:
  - Vector for point 1. $...\vec{p_0} ( x_0, y_0 )$
  - Vector for point 2. $...\vec{p_1} ( x_1, y_1 )$
- Return:
  - [ Array of x values, Array of y values ] $...\vec{Y} = f ( \vec{X} )$ 

The functions may be tested by setting up input vectors that represent turning points through which the function passes. 

```python
# Test parametric cubic polynomial 

v0   = [  0.2 ,  0.2  ]
v1   = [  0.8 ,  0.8  ]
data = cubic_segment ( v0, v1 )
```

```python
# Test parametric sine function.

v0 = [  1.0 , -0.75  ]
v1 = [  4.0 ,  0.5   ]
data = sin_segment ( v0, v1 )
```

### Parametric Function Return Data

Output data is returned as two arrays, one for the function domain (independent variable), and range (dependent variable).
- In terms of notation, we'll express the domain for linear algebraic functions as $x$, and for trigonometric functions, we'll express it as $t$.
- In the example below, we will use the data to plot the computed parametric functions.
- See the implementation of the `plot_function` for the details of the plots shown below. 
  
```python
# Test parametric cubic polynomial function.

v0   = [  0.2 ,  0.2  ]
v1   = [  0.8 ,  0.8  ]
data = cubic_segment ( v0, v1 )

# Plot the computed function.

lim_x = [  0.0,  1.0  ]
lim_y = [  0.0,  1.0  ]
plot_function (
    data,
    [ v0, v1 ],
    [ lim_x, lim_y ],
    'Parametric Cubic Polynomial', 'f(x) = a·x³ + b·x² + c·x + d'
) 
```
![Image](images/figure_1.png)

```python
# Test parametric sine function.

v0 = [  1.0 , -0.75  ]
v1 = [  4.0 ,  0.5   ]
data = sin_segment ( v0, v1 )

# Plot the computed function.

lim_x = [  0, 2*PI ]
lim_y = [ -1, 1    ]
plot_function (
    data,
    [ v0, v1 ],
    [ lim_x, lim_y ],
    'Parametric Sine Function',
    'f(t) = a·sin( w·(t - p) ) + c'
) 
```
![Image](images/figure_2.png)

### Symbolic Solution to Parametric Cubic Polynomial

The `solve_cubic_coefficients` function uses the Python package `sympy`, to implement a symbolic solution for the coefficients of a cubic polynomial, given two turning points.
``` Python
solve_cubic_coefficients ()
```

``` Terminal
             -2⋅y₀ + 2⋅y₁
a = ───────────────────────────────
      3       2             2     3
    x₀  - 3⋅x₀ ⋅x₁ + 3⋅x₀⋅x₁  - x₁


    3⋅x₀⋅y₀ - 3⋅x₀⋅y₁ + 3⋅x₁⋅y₀ - 3⋅x₁⋅y₁
b = ─────────────────────────────────────
         3       2             2     3
       x₀  - 3⋅x₀ ⋅x₁ + 3⋅x₀⋅x₁  - x₁


       -6⋅x₀⋅x₁⋅y₀ + 6⋅x₀⋅x₁⋅y₁
c = ───────────────────────────────
      3       2             2     3
    x₀  - 3⋅x₀ ⋅x₁ + 3⋅x₀⋅x₁  - x₁


      3          2                2        3
    x₀ ⋅y₁ - 3⋅x₀ ⋅x₁⋅y₁ + 3⋅x₀⋅x₁ ⋅y₀ - x₁ ⋅y₀
d = ───────────────────────────────────────────
            3       2             2     3
          x₀  - 3⋅x₀ ⋅x₁ + 3⋅x₀⋅x₁  - x₁
```

## Mathematical principles

### Parametric Solutions for Cubic Polynomial Coefficient

- Given:

$$f(x) = a x^3 + b x^2 + c x + d \quad \quad ...Cubic \hspace{2mm} polynomial function.$$ 

$$f'(x) = \dfrac{dy}{dx}  = 3 a x^2 + 2 b x + c \quad \quad ...Derivative \hspace{2mm} of f.$$ 

- System of equations to solve:

$$ y_0 = a x_0^3 + b x_0^2 + c x_0 + d \quad \quad ...(1) \quad f(x) \hspace{2mm} passes \hspace{2mm} through \hspace{2mm} p_0. $$

$$ y_1 = a x_1^3 + b x_1^2 + c x_1 + d \quad \quad ...(2) \quad f(x) \hspace{2mm} passes \hspace{2mm} through \hspace{2mm} p_1. $$

$$ 0 = 3 a x_0^2 + 2 b x_0 + c \quad \quad ...(3) \quad Gradient \hspace{2mm} is \hspace{2mm} zero \hspace{2mm} at \hspace{2mm} p_0, \hspace{2mm} f'(x_0) = 0 $$

$$ 0 = 3 a x_1^2 + 2 b x_1 + c \quad \quad ...(4) \quad Gradient \hspace{2mm} is \hspace{2mm} zero \hspace{2mm} at \hspace{2mm} p_1, \hspace{2mm} f'(x_1) = 0 $$

### Parametric Solutions for Sine Function Parameters




## Contributing
Contributions are welcome! Please follow the contribution guidelines.
1. Fork the project.
2. Create your feature branch (git checkout -b feature/AmazingFeature).
3. Commit your changes (git commit -m 'Add some AmazingFeature').
4. Push to the branch (git push origin feature/AmazingFeature).
5. Open a pull request.

## License
Distributed under the MIT License. See LICENSE for more information.

## Contact Information
- Twitter: [@rohingosling](https://x.com/rohingosling)
- Project Link: [https://github.com/your-username/your-repo](https://github.com/rohingosling/pinger)

## Acknowledgments
- [ping3](https://github.com/kyan001/ping3)
