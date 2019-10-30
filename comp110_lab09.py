"""
Module: comp110_lab09

Code for COMP110 Lab Session 09 (Dictionaries and Elections)

Authors:
1) Name - USD Email Address
2) Name - USD Email Address
"""



def get_election_results(election_filename):
    """ Replace this with a docstring comment with the correct format. """

    return None  # replace this line with your implemenation


def main():
    """
    Gets election data from a file, then creates a pie chart showing results for
    a user-entered region.
    """

    election_filename = input("Enter the name of the election data file: ")

    # To Do: Step 1 - Use your get_election_results to get a dictionary with
    # data


    region_name = input("Enter the name of the state you want to graph: ")

    # To Do: Step 2 - Validate that the user-entered region name is a valid one
    # For example, "California" is valid while "Jefferson" is not valid.
    # You should continually re-prompt the user to enter a region name until
    # they enter a valid one.
    # Hint: the "in" operator will be very helpful here.


    # To Do: Step 3 - Use pyplot's pie function to make a pie chart out of the
    # election data for the user-entered region.
    # Each wedge of the pie should be labeled with the candidate's name and
    # should have the "traditional" coloring (red for Republican, blue for
    # Democratic, and white for third-party/other).


"""
WARNING: Do NOT modify anything below this point.
"""
if __name__ == "__main__":
    main()
