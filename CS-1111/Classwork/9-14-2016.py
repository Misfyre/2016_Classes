__author__ = "Nick Sarris (ngs5st)"

def create_dictionary():

    number_of_entries = input("How many entries do you want to add?: ")
    experience_dict = dict()
    print ('')
    i = 0

    while i < int(number_of_entries):

        job_title = input("Enter the name of your job: ")
        company_name = input("Enter the name of your company: ")
        year = input("Enter the year that you worked: ")
        print ('')

        experience_dict[year] = job_title, company_name
        i += 1

    return experience_dict

def scores():

    number_of_entries = input("How many entries do you want to add?: ")
    score_list = list()
    print ('')
    i = 0

    while i < int(number_of_entries):

        score_input = input("Enter your score to add: ")
        list.append(score_list, int(score_input))
        i += 1

    score_list.remove(min(score_list))
    average = sum(score_list) / len(score_list)
    return average

if __name__ == "__main__":
    average = scores()
    print (average)