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


## Mathematical principles


### Parametric Solutions for Cubic Polynomial Coefficient

- Note:
  - Parameters computed using symbolic solver from the Python `sympy` package.
  - In the code, the `solve_cubic_coefficients()` function implements the `sympy` symbolic solution to compute the coeficients.
  
- Given:

$$f(x) = a x^3 + b x^2 + c x + d \quad \quad ...Cubic \hspace{2mm} polynomial function.$$ 

$$f'(x) = \dfrac{dy}{dx}  = 3 a x^2 + 2 b x + c \quad \quad ...Derivative \hspace{2mm} of \hspace{2mm} f_x. \hspace{1.3cm} $$

$$ p_0 ( x_0, y_0 ) \quad \quad ...First \hspace{2mm} turning \hspace{2mm} point. \hspace{2.8cm} $$

$$ p_1 ( x_1, y_1 ) \quad \quad ...Second \hspace{2mm} turning \hspace{2mm} point. \hspace{2.5cm} $$

- System of equations to solve:

$$ y_0 = a x_0^3 + b x_0^2 + c x_0 + d \quad \quad ...(1) \quad f_x \hspace{2mm} passes \hspace{2mm} through \hspace{2mm} p_0. \hspace{2mm} f(x_0) = y_0 \hspace{1.5cm} $$

$$ y_1 = a x_1^3 + b x_1^2 + c x_1 + d \quad \quad ...(2) \quad f_x \hspace{2mm} passes \hspace{2mm} through \hspace{2mm} p_1. \hspace{2mm} f(x_1) = y_1 \hspace{1.5cm} $$

$$ 0 = 3 a x_0^2 + 2 b x_0 + c \quad \quad ...(3) \quad Gradient \hspace{2mm} of \hspace{2mm} f_x \hspace{2mm} is \hspace{2mm} zero \hspace{2mm} at \hspace{2mm} p_0. \hspace{2mm} f'(x_0) = 0 $$

$$ 0 = 3 a x_1^2 + 2 b x_1 + c \quad \quad ...(4) \quad Gradient \hspace{2mm} of \hspace{2mm} f_x \hspace{2mm} is \hspace{2mm} zero \hspace{2mm} at \hspace{2mm} p_1. \hspace{2mm} f'(x_1) = 0 $$

- Constraints:

$$ 0 \leq x_0 \leq x_1 \quad \quad ...p_0 \hspace{2mm} comes \hspace{2mm} before \hspace{2mm} p_1. \hspace{3.6cm} $$

$$ y_0 \neq y_1 \quad \quad ...P_0 \hspace{2mm} and \hspace{2mm} P_1 \hspace{2mm} are \hspace{2mm} not \hspace{2mm} in \hspace{2mm} the \hspace{2mm} same \hspace{2mm} place. $$

- Coefficient (Paramter) Solutions:

$$ a = \dfrac{ 2 y_1 - 2 y_0 }{ x_0^3 - 3 x_1 x_0^2 + 3 x_0 x_1^2 - x_1^3 } $$

$$ b = \dfrac{ 3 x_0 y_0 - 3 x_0 y_1 + 3 x_1 y_0 - 3 x_1 y_1 }{ x_0^3 - 3 x_1 x_0^2 + 3 x_0 x_1^2 - x_1^3 } $$

$$ c = \dfrac{ 6 x_0 x_1 y_1 + 6 x_0 x_1 y_0 }{ x_0^3 - 3 x_1 x_0^2 + 3 x_0 x_1^2 - x_1^3 } $$

$$ d = \dfrac{ y_1 x_0^3 + 3 x_1 y_1 x_0^2 + 3 x_0 x_1 y_0^2 - x_1 y_0^3 }{ x_0^3 - 3 x_1 x_0^2 + 3 x_0 x_1^2 - x_1^3 } $$


### Parametric Solutions for Sine Function Parameters

- Note:
  - Parameters computed intuitively. No need to formally solve the system of equations.  

- Given:

$$ f(t) = a \cdot sin \left( w \cdot ( t - p ) \right) + c \quad \quad ...Parametric \hspace{2mm} sine function.$$ 

$$ f'(t) = a \cdot w  \cdot cos \left( w  \cdot ( t - p ) \right) \quad \quad ...Derivative \hspace{2mm} of \hspace{2mm} f_t. \hspace{1.6cm} $$

- System of equations to solve:

$$ f(x_0) = y_0 \quad \quad ...(1) \quad f_x \hspace{2mm} passes \hspace{2mm} through \hspace{2mm} p_0. \hspace{1.5cm} $$

$$ f(x_1) = y_1 \quad \quad ...(2) \quad f_x \hspace{2mm} passes \hspace{2mm} through \hspace{2mm} p_1. \hspace{1.5cm} $$

$$ f'(x_0) = 0 \quad \quad ...(3) \quad Gradient \hspace{2mm} of \hspace{2mm} f_x \hspace{2mm} is \hspace{2mm} zero \hspace{2mm} at \hspace{2mm} p_0. \hspace{2mm} $$

$$ f'(x_1) = 0 \quad \quad ...(4) \quad Gradient \hspace{2mm} of \hspace{2mm} f_x \hspace{2mm} is \hspace{2mm} zero \hspace{2mm} at \hspace{2mm} p_1. \hspace{2mm} $$

- Constraints:

$$ 0 \leq x_0 \leq x_1 \quad \quad ...p_0 \hspace{2mm} comes \hspace{2mm} before \hspace{2mm} p_1. \hspace{3.6cm} $$

$$ y_0 \neq y_1 \quad \quad ...P_0 \hspace{2mm} and \hspace{2mm} P_1 \hspace{2mm} are \hspace{2mm} not \hspace{2mm} in \hspace{2mm} the \hspace{2mm} same \hspace{2mm} place. $$

- Paramter Solutions:

$$ a = - \dfrac{ y_1 - y_0 }{ 2 } \quad \quad ...Amplitude. \hspace{6cm} $$

$$ w = \dfrac{ \pi }{ t_1 - t_0 } \quad \quad ...Frequency. \hspace{6.5cm} $$

$$ p = t_0 - \dfrac{ \pi }{ 2 \cdot w } \quad \quad ...Phase \hspace{2mm} shift. \hspace{2mm} i.e. \hspace{2mm} Horizontal \hspace{2mm} displacement. $$

$$ c = \dfrac{ y_1 + y_0 }{ 2 } \quad \quad ...Vertical\hspace{2mm}shift.\hspace{2mm}i.e.\hspace{2mm}Vertical\hspace{2mm}displacement. $$


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
- Project Link: [https://github.com/rohingosling/parametric-functions/tree/main](https://github.com/rohingosling/parametric-functions/tree/main)



## Acknowledgments
- N/A
