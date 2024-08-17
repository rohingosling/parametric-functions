#-------------------------------------------------------------------------------------------------------------------------------------------------------------
# Program: Parametric Function Test
# Version: 1.0
# Author:  Rohin Gosling
#
# Description:
# - Test program used to test parametric Sine and cubic polynomial function.
#
#   f(x) = a·x³ + b·x² + c·x + d 
#
#   f(t) = a·sin(w·(t-p)) + c
#
#-------------------------------------------------------------------------------------------------------------------------------------------------------------

import numpy             as np
import sympy             as sp
import matplotlib.pyplot as plt

#-------------------------------------------------------------------------------------------------------------------------------------------------------------
# Solve Cubic Polynomial Coefficients. 
#
# Use the `sympy` symbolic math engine, to solve for the coefficients of a cubic polynomial, given two turning points p₀ and p₁.
# 
# 
#   Cubic Polynomial function:
# 
#      f(x) = a·x³ + b·x² + c·x + d
#
# 
#   Derivitive of f:
#
#             dy
#     f'(x) = ── = 3·a·x² + 2·b·x + c  
#             dx                       
#
# 
#   System of equations to solve:
#                                                 ╮ 
#        y₀ = a·x₀³ + b·x₀² + c·x₀ + d    ...(1)  │
#                                                 ├  f(x) passes through p₀ and p₁.
#        y₁ = a·x₁³ + b·x₁² + c·x₁ + d    ...(2)  │
#                                                 ╯
#                                                 ╮ 
#         0 = 3·a·x₀² + 2·b·x₀ + c        ...(3)  │  p₀ and p₁ are the turning points of f.
#                                                 ├  i.e. The gradient f' of f is zero at p₀ and p₁. 
#         0 = 3·a·x₁² + 2·b·x₁ + c        ...(4)  │       f'(x) = 0, for x₀ and x₁.
#                                                 ╯
#
#    Constraints:
#
#        x₀ < x₁    ...p₀ is positioned to the left of p₁.
#
#        y₀ ≠ y₁    ...p₀ and p₁ may not be in the same position.  
#
#                                                 
#   Solutions:
#
#                      2⋅y₁ - 2⋅y₀
#         a = ─────────────────────────────
#             x₀³ - 3⋅x₀²⋅x₁ + 3⋅x₀⋅x₁² - x₁³
#
#         
#             3⋅x₀⋅y₀ - 3⋅x₀⋅y₁ + 3⋅x₁⋅y₀ - 3⋅x₁⋅y₁
#         b = ─────────────────────────────────
#                x₀³ - 3⋅x₀²⋅x₁ + 3⋅x₀⋅x₁² - x₁³
#         
#         
#                 6⋅x₀⋅x₁⋅y₁ - 6⋅x₀⋅x₁⋅y₀
#         c = ─────────────────────────────
#             x₀³ - 3⋅x₀²⋅x₁ + 3⋅x₀⋅x₁² - x₁³
#         
#
#             x₀³⋅y₁ - 3⋅x₀²⋅x₁⋅y₁ + 3⋅x₀⋅x₁⋅y₀² - x₁⋅y₀³
#         d = ───────────────────────────────────────
#                   x₀³ - 3⋅x₀²⋅x₁ + 3⋅x₀⋅x₁² - x₁³
#
#
#-------------------------------------------------------------------------------------------------------------------------------------------------------------

def solve_cubic_coefficients ():

    # Define local constants.

    PRINT_NOTATION_FORMATTED = True
    PRINT_NOTATION_CODE      = False

    # Define the symbols.

    a, b, c, d        = sp.symbols ( 'a b c d' )
    x, x0, x1, y0, y1 = sp.symbols ( 'x x0 x1 y0 y1' )

    # Define the function f(x).

    f = a*x**3 + b*x**2 + c*x + d

    # Define the derivative f'(x).

    df = sp.diff ( f, x )

    # Set up system of equations to solve. 

    eq1 = sp.Eq (  f.subs ( x, x0 ), y0 )
    eq2 = sp.Eq (  f.subs ( x, x1 ), y1 )
    eq3 = sp.Eq ( df.subs ( x, x0 ), 0  )
    eq4 = sp.Eq ( df.subs ( x, x1 ), 0  )

    # Solve the system of equations.

    solutions = sp.solve ( [ eq1, eq2, eq3, eq4 ], ( a, b, c, d ) )

    # Display the solutions.

    print ()

    if PRINT_NOTATION_FORMATTED:
        for solution in solutions:
            sp.pprint ( sp.Eq ( solution,  solutions [ solution ] ) )
            print ( "\n" )

    if PRINT_NOTATION_CODE:
        for solution in solutions:
            print ( sp.Eq ( solution,  solutions [ solution ] ) )
            print ( "\n" )

#-------------------------------------------------------------------------------------------------------------------------------------------------------------
# Cubic polynomial function segment. 
#
# f(x) = a·x³ + b·x² + c·x + d
#
#-------------------------------------------------------------------------------------------------------------------------------------------------------------

def cubic_segment ( v0, v1 ):

    # Define local constants
    
    X  = 0          # Vector x element index. pₓ = v[0]
    Y  = 1          # Vector y element index. pᵧ = v[1]

    # Define lambdas.    

    f = lambda x : a*x**3 + b*x**2 + c*x + d        # f(x) = a·x³ + b·x² + c·x + d

    # Initialise coordinates from input vectors. 

    x0 =  v0 [ X ]
    y0 =  v0 [ Y ]

    x1 =  v1 [ X ]
    y1 =  v1 [ Y ]

    # Compute solutions for cubic polynomial function coefficients.
    #
    #   f(x) = a·x³ + b·x² + c·x + d
    #
    #
    #                   2⋅y₁ - 2⋅y₀
    #      a = ─────────────────────────────
    #          x₀³ - 3⋅x₁⋅x₀² + 3⋅x₀⋅x₁² - x₁³
    #
    #         
    #          3⋅x₀⋅y₀ - 3⋅x₀⋅y₁ + 3⋅x₁⋅y₀ - 3⋅x₁⋅y₁
    #      b = ─────────────────────────────────
    #            x₀³ - 3⋅x₁⋅x₀² + 3⋅x₀⋅x₁² - x₁³
    #         
    #         
    #              6⋅x₀⋅x₁⋅y₁ - 6⋅x₀⋅x₁⋅y₀
    #      c = ─────────────────────────────
    #          x₀³ - 3⋅x₁⋅x₀² + 3⋅x₀⋅x₁² - x₁³
    #          
    #
    #          y₁⋅x₀³ - 3⋅x₁⋅y₁⋅x₀² + 3⋅x₀⋅x₁⋅y₀² - x₁⋅y₀³
    #      d = ───────────────────────────────────────
    #               x₀³ - 3⋅x₁⋅x₀² + 3⋅x₀⋅x₁² - x₁³
    #     

    # Compute coefficient substitutions.
    
    dx = x0**3 - 3*x1*x0**2 + 3*x0*x1**2 - x1**3

    # Compute coefficients. 

    a =                                        ( -2*y0 + 2*y1 ) / dx
    b =               ( 3*x0*y0 - 3*x0*y1 + 3*x1*y0 - 3*x1*y1 ) / dx 
    c =                            ( -6*x0*x1*y0 + 6*x0*x1*y1 ) / dx
    d = ( y1*x0**3 - 3*x1*y1*x0**2 + 3*x0*y0*x1**2 - y0*x1**3 ) / dx

    # Generate function data.
    
    domain_left  = 0.0      # Domain, from 0.0
    domain_right = 1.0      #         to   1.0
    point_count  = 9 * 100  # Nine point base resolution, multiplied by upsample factor.                             

    domain = np.linspace ( domain_left, domain_right, point_count )     # x values.
    range  = f ( domain )                                               # y values. 

    # Return data to caller. 

    return [ domain, range ]

#-------------------------------------------------------------------------------------------------------------------------------------------------------------
# Sin function segment. 
#
# f(t) = a·sin( w·( t - p ) ) + c
#
#-------------------------------------------------------------------------------------------------------------------------------------------------------------

def sin_segment ( v0, v1 ):

    # Define local constants

    PI = np.pi      # Value of π.
    X  = 0          # Vector x element index. pₓ = v[0]
    Y  = 1          # Vector y element index. pᵧ = v[1]

    # Define lambdas.
    #      y = sin(t)              ...Standard sin function.
    #   f(t) = a·sin(w·(t-p)) + c  ...Parametric sin function. 

    sin = lambda t : np.sin ( t )
    f   = lambda t : a * sin ( w * ( t - p ) ) + c      

    # Initialise coordinates from input vectors. 

    t0 =  v0 [ X ]
    y0 =  v0 [ Y ]

    t1 =  v1 [ X ]
    y1 =  v1 [ Y ]

    # Compute solutions for parametric sin function parameters.
    #
    #   f(t) = a·sin( w·( t - p ) ) + c
    #
    #
    #             y₁ - y₀
    #      a = - ─────────    ...Amplitude
    #                2
    #
    #              π
    #      w = ─────────      ...Frequency 
    #           t₁ - t₀ 
    #
    #                 π
    #      p = t₀ - ─────     ...Phase shift. i.e. Horizontal displacement. 
    #                2·w    
    #          
    #           y₁ + y₀
    #      c = ─────────      ...Vertical shift. i.e. Vertical displacement. 
    #              2
    #

    a = -( y1 - y0 ) / 2                # Amplitude.
    w =           PI / ( t1 - t0 )      # Frequency.
    p =      t0 - PI / ( 2 * w )        # Phase shift.    i.e. Horizontal displacement.  
    c =  ( y1 + y0 ) / 2                # Vertical shift. i.e. Vertical displacement.  

    # Generate function data.
    
    domain_left  = 0        # Domain, from 0   degrees. 
    domain_right = 2 * PI   #         to   360 degrees. 
    point_count  = 9 * 100  # Nine point base resolution, multiplied by upsample factor, i.e. 9 x 100.
                            #                                                                   
                            #   1 |           .   ■   .                                   y = sin t                                    
                            #     |       ■               ■       
                            #     |   .                       .                                      
                            #     |      
                            #   0 ■-------|-------|-------|-------■-------|-------|-------|-------■    t    
                            #     0     ¹⁄₄·π   ¹⁄₂·π   ³⁄₄·π     π     ⁵⁄₄·π   ³⁄₂·π   ⁷⁄₄·π    2·π
                            #     |                                   '                       '   
                            #     |                                       ■               ■                                      
                            #  -1 |                                           '   ■   '      
                            #
                            #     y          

    domain = np.linspace ( domain_left, domain_right, point_count )     # t values.
    range  = f ( domain )                                               # y values. 

    # Return data to caller. 

    return [ domain, range ]


#-------------------------------------------------------------------------------------------------------------------------------------------------------------
# plot function.
#-------------------------------------------------------------------------------------------------------------------------------------------------------------

def plot_function ( data, v, lim, text_title, text_function_label ):

    # Define local constants
    
    PI       = np.pi      # Value of π.
    X        = 0          # Domain index.
    Y        = 1          # Range index. 
    DOT_RED  = 'ro'       # matplotlib.plot graph dot, color red.
    DOT_BLUE = 'bo'       # matplotlib.plot graph dot, color blue.

    # Initialise coordinates from input vectors. 

    t0 =  v [ 0 ][ X ]
    y0 =  v [ 0 ][ Y ]

    t1 =  v [ 1 ][ X ]
    y1 =  v [ 1 ][ Y ]

    # Plot the function.

    plt.plot ( data [ X ], data [ Y ], color = 'black', label = text_function_label )

    # Plot the points v0 and v1.

    plt.plot ( t0, y0, DOT_RED  )
    plt.plot ( t1, y1, DOT_BLUE )

    # Annotate the points.

    plt.text ( t0, y0 + 0.1, f'v₀({float(t0):.3}, {float(y0):.3})', color = 'red'  )
    plt.text ( t1, y1 - 0.1, f'v₁({float(t1):.3}, {float(y1):.3})', color = 'blue' )

    # Add labels and title.

    plt.xlabel  ( 't' )
    plt.ylabel  ( 'f(t)' )
    plt.title   ( text_title )
    plt.axhline ( 0, color = 'black', linewidth = 0.5 )
    plt.axvline ( 0, color = 'black', linewidth = 0.5 )

    # Set the y-axis range from -1 to 1.
    
    plt.xlim ( lim [ X ] )
    plt.ylim ( lim [ Y ] )

    # Add a legend.

    plt.legend ()

    # Show the plot.

    plt.grid ( True )
    plt.show ()


#-------------------------------------------------------------------------------------------------------------------------------------------------------------
# Main function.
#-------------------------------------------------------------------------------------------------------------------------------------------------------------

def main ():

    # Define local constants. 

    PI = np.pi      # Value of π.    

    # Solve cubic polynomial coefficients.

    solve_cubic_coefficients ()

    # Test parametric cubic polynomial function.    
    # - Initialise test vertices v₀ and v₁.
    # - Initialise graph domain and range limit vectors.

    v0 = [  0.2 ,  0.2  ]
    v1 = [  0.8 ,  0.8  ]

    lim_x = [  0.0,  1.0  ]
    lim_y = [  0.0,  1.0  ]

    data = cubic_segment ( v0, v1 )

    plot_function ( data, [ v0, v1 ], [ lim_x, lim_y ], 'Parametric Cubic Polynomial', 'f(x) = a·x³ + b·x² + c·x + d' ) 

    # Test parametric sin segment function.    
    # - Initialise test vertices v₀ and v₁.
    # - Initialise graph domain and range limit vectors.
    
    v0 = [  1.0 , -0.25  ]
    v1 = [  3.0 ,  0.75  ]

    lim_x = [  0, 2*PI ]
    lim_y = [ -1, 1    ]

    data = sin_segment ( v0, v1 )

    plot_function ( data, [ v0, v1 ], [ lim_x, lim_y ], 'Parametric Sine Function', 'f(t) = a·sin( w·(t - p) ) + c' ) 

#-------------------------------------------------------------------------------------------------------------------------------------------------------------
# Program entry point. 
#-------------------------------------------------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":

    main ()
    

