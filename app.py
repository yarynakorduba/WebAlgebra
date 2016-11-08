from flask import Flask, render_template, request
from inverse_via_lu import Matrix
app = Flask(__name__)

def to_matrix(s):
    matrix = []
    lines = s.split('\n')
    for l in lines:
        matrix.append(list(map(float, l.split())))

    return matrix

def matrix_to_sring(m):
    new_matrix = '$\\left(\\begin{matrix}\n'
    for el in range(len(m)):
        answer = ''
        for ele in range(len(m[el])):
            if m[el][ele] == int(m[el][ele]):
                answer += str(m[el][ele])[:-2]
            else:
                answer += str(round(m[el][ele], 3))

            if ele != (len(m[el])-1):
                answer += '&'

            else:
                answer += '\\\\\n'

        new_matrix += answer
    new_matrix += '\\end{matrix}\\right)$\n'
    return new_matrix



@app.route('/', methods=["GET", "POST"])
def get_index():
    if request.method == "POST":
        matrix = request.form['matrix']
        new_matrix = Matrix(to_matrix(matrix))
        new_matrix = new_matrix.matrix_inverse()
     #   new_matrix = '$\\left(\\begin{matrix}\n'
        new_matrix = matrix_to_sring(new_matrix)
        return render_template('index.html', matrix=matrix, new_matrix=new_matrix)
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug = True)