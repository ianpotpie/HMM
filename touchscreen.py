# Implement part 2 here!


class touchscreenHMM:

    # You may add instance variables, but you may not create a
    # custom initializer; touchscreenHMMs will be initialized
    # with no arguments.

    def __init__(self, width=20, height=20):
        """
        Feel free to initialize things in here!
        """
        self.width = width
        self.height = height
        # Write your code here!
        pass

    def sensor_model(self, observation, state):
        """
        Feel free to change the parameters of this function as you see fit.
        You may even delete this function! It is only here to point you
        in the right direction.

        This is the sensor model to get the probability of getting an observation from a state
        """
        # Write your code here!
        return None

    def transition_model(self, old_state, new_state):
        """
        Feel free to change the parameters of this function as you see fit.
        You may even delete this function! It is only here to point you
        in the right direction.

        This will be your transition model to go from the old state to the new state
        """
        # Write your code here!
        return None

    def prior_model(self, first_state):
        """
        Feel free to change the parameters of this function as you see fit.
        You may even delete this function! It is only here to point you
        in the right direction.

        This will be your prior_model, which returns the initial probability distribution of 
        the states at time t = 0.
        """
        # Write your code here!
        return None

    def filter_noisy_data(self, frame):
        """
        This is the function we will be calling during grading, passing in a noisy simualation. It should return the
        distribution where you think the actual position of the finger is in the same format that it is passed in as.

        DO NOT CHANGE THE FUNCTION PARAMETERS

        :param frame: A noisy frame to filter. 
                     (Recall: A frame is a 2D numpy array filled with 0s, and a single 1 denoting a touch location.)
        :return: A 2D numpy array with the probabilities of the actual finger location.
        """
        # Write your code here!
        return frame
