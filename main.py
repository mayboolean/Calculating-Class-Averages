def calculate_class_averages(classrooms):
    class_averages = {}
    for subject, students_scores in classrooms.items():
        # print(subject)
        # print(students_scores)
        scores_list = []
        if not students_scores:
            class_averages[subject] = 0
            continue
        for scores in students_scores.values():
            scores_list += scores
        avg = sum(scores_list)/len(scores_list)
        avg = round(avg,2)
        class_averages[subject] = avg
    print(class_averages)        
    return(class_averages)






            



school_scores = {
        "Math": {},
        "Science": {
            "Alice": [80, 85, 88],
            "Bob": [78, 82, 85]
        }
    }

result = calculate_class_averages(school_scores)


  # for subject in classrooms:
    #     subject_scores = classrooms[subject]
    #     subject_score_list = []
    #     for student, scores in subject_scores.items():
    #         if not student:
    #             avg[subject] = 0
    #         subject_score_list += scores

    #     average = sum(subject_score_list)/len(subject_score_list)
    #     average = round(average,2)
    #     avg[subject] = average
    # return avg