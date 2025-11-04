from pyscript import document, display

def print_grade(e):
    firstname = document.getElementById("firstname").value
    lastname = document.getElementById("lastname").value
    sci = int(document.getElementById("sci").value)
    math = int(document.getElementById("math").value)
    eng = int(document.getElementById("eng").value)
    fil = int(document.getElementById("fil").value)
    tle = int(document.getElementById("tle").value)
    pe = int(document.getElementById("pe").value)

    grades = [sci, math, eng, fil, tle, pe]
    avggrade = round(sum(grades) / len(grades), 2)

    # Create a formatted HTML string for the grades
    all_grades = f"""
    <p>
        Science: {sci}<br>
        Math: {math}<br>
        English: {eng}<br>
        Filipino: {fil}<br>
        TLE: {tle}<br>
        PE: {pe}
    </p>
    """

    # Display results with HTML rendering
    document.getElementById("name").innerHTML = f"<b>Name:</b> {firstname} {lastname}"
    document.getElementById("grades").innerHTML = all_grades
    document.getElementById("average").innerHTML = f"<b>Your general weighted average is {avggrade}</b>"
