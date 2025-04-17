// Step 1: Install dependencies from requirements.txt
def install = "pip install -r requirements.txt".execute()
install.waitFor()

println "Installing dependencies..."
println install.in.text
if (install.exitValue() != 0) {
    println "Error during install:\n${install.err.text}"
    System.exit(1)
}

// Step 2: Run the Flask app
println "Running Flask app..."
def runApp = "python3 main.py".execute()
runApp.waitFor()

println "Flask Output:\n${runApp.in.text}"
println "Flask Errors:\n${runApp.err.text}"
