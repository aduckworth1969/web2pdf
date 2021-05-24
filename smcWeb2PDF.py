@auth.requires(auth.has_membership('Faculty') or auth.has_membership('Administrators'))
def find_replace_google_run(current_course, current_course_name, export_format):
    ret = "Running...<br /><br />"

    # Regular expression to find websites and exclude google docs, YouTube...
    find_str = r'''https://www[.]^(?!.*google)[.]com'''

    # === Pull all pages and extract links ===
    items = Canvas.get_page_list_for_course(current_course)
    total_pages = len(items)
    for i in items:
        orig_text = items[i]
        new_text = orig_text
        page_changed = False
        ret += "<br />Working on Page: " + str(i)

        matches = re.finditer(find_str, new_text)
        match_count = 0
        for m in matches:
            match_count += 1
            # Dl this doc and then do a replace.
            doc_url = m.group(0)
            print("found url: " + str(doc_url))
            smc_url = find_replace_google_download_doc(current_course_name, export_format, doc_url)
            if smc_url != "":
                new_text = new_text.replace(doc_url, smc_url)
                page_changed = True
            else:
                print("error getting smc url for google doc " + str(doc_url))

        # Update page
        if page_changed is True:
            new_item = dict()
            new_item["wiki_page[body]"] = new_text
            Canvas.update_page_for_course(current_course, i, new_item)
            ret += " page updated with " + str(match_count) + " changes."
        else:
            ret += " no links found."

    # === Pull all quizzes and extract links ===
    items = Canvas.get_quiz_list_for_course(current_course)
    total_quizzes = len(items)
    for i in items:
        orig_text = items[i]
        new_text = orig_text
        page_changed = False
        ret += "<br />Working on Quiz: " + str(i)

        matches = re.finditer(find_str, new_text)
        match_count = 0
        for m in matches:
            match_count += 1
            # Dl this doc and then do a replace.
            doc_url = m.group(0)
            print("found url: " + str(doc_url))
            smc_url = find_replace_google_download_doc(current_course_name, export_format, doc_url)
            if smc_url != "":
                new_text = new_text.replace(doc_url, smc_url)
                page_changed = True
            else:
                print("error getting smc url for google doc " + str(doc_url))

        # Update
        if page_changed is True:
            new_item = dict()
            new_item["quiz[description]"] = new_text
            Canvas.update_quiz_for_course(current_course, i, new_item)
            ret += " quiz updated with " + str(match_count) + " changes."
        else:
            ret += " no links found."

        quiz_id = i
        # === Pull all questions and extract links ===
        q_items = Canvas.get_quiz_questions_for_quiz(current_course, quiz_id)
        total_questions = len(q_items)
        for q in q_items:
            q_orig_text = q_items[q]
            q_new_text = q_orig_text
            q_page_changed = False
            ret += "<br />&nbsp;&nbsp;&nbsp;&nbsp;Working on question: " + str(q)

            q_matches = re.finditer(find_str, q_new_text)
            q_match_count = 0
            for q_m in q_matches:
                q_match_count += 1
                # Dl this doc and then do a replace.
                q_doc_url = q_m.group(0)
                print("found url: " + str(q_doc_url))
                q_smc_url = find_replace_google_download_doc(current_course_name, export_format, q_doc_url)
                if q_smc_url != "":
                    q_new_text = q_new_text.replace(q_doc_url, q_smc_url)
                    q_page_changed = True
                else:
                    print("error getting smc url for google doc " + str(q_doc_url))

            # Update page
            if q_page_changed is True:
                new_item = dict()
                new_item["question[question_text]"] = q_new_text
                Canvas.update_quiz_question_for_course(current_course, quiz_id, q, new_item)
                ret += " question updated with " + str(q_match_count) + " changes."
            else:
                ret += " no links found."

    # === Pull all discussion topics and extract links ===
    items = Canvas.get_discussion_list_for_course(current_course)
    total_dicussions = len(items)
    for i in items:
        orig_text = items[i]
        new_text = orig_text
        page_changed = False
        ret += "<br />Working on Discussion: " + str(i)

        matches = re.finditer(find_str, new_text)
        match_count = 0
        for m in matches:
            match_count += 1
            # Dl this doc and then do a replace.
            doc_url = m.group(0)
            print("found url: " + str(doc_url))
            smc_url = find_replace_google_download_doc(current_course_name, export_format, doc_url)
            if smc_url != "":
                new_text = new_text.replace(doc_url, smc_url)
                page_changed = True
            else:
                print("error getting smc url for google doc " + str(doc_url))

        # Update page
        if page_changed is True:
            new_item = dict()
            new_item["message"] = new_text
            Canvas.update_discussion_for_course(current_course, i, new_item)
            ret += " discussion updated with " + str(match_count) + " changes."
        else:
            ret += " no links found."

    # === Pull all assignments and extract links ===
    items = Canvas.get_assignment_list_for_course(current_course)
    total_assignments = len(items)
    for i in items:
        orig_text = items[i]
        new_text = orig_text
        page_changed = False
        ret += "<br />Working on Assignment: " + str(i)

        matches = re.finditer(find_str, new_text)
        match_count = 0
        for m in matches:
            match_count += 1
            # Dl this doc and then do a replace.
            doc_url = m.group(0)
            print("found url: " + str(doc_url))
            smc_url = find_replace_google_download_doc(current_course_name, export_format, doc_url)
            if smc_url != "":
                new_text = new_text.replace(doc_url, smc_url)
                page_changed = True
            else:
                print("error getting smc url for google doc " + str(doc_url))

        # Update page
        if page_changed is True:
            new_item = dict()
            new_item["assignment[description]"] = new_text
            Canvas.update_assignment_for_course(current_course, i, new_item)
            ret += " assignment updated with " + str(match_count) + " changes."
        else:
            ret += " no links found."

    ret += "<br /><br /><b>Done!</b>"
    return ret