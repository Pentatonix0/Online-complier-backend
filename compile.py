from flask_restx import Resource, Namespace, fields
from flask import request
from judge0API import Judge0API

compile_ns = Namespace(
    "compilation", description="A namespace for compilation tools")

get_submission_model = compile_ns.model(
    "GetProgramSubmission",
    {
        "source_code": fields.String(required=True, description="Program's source code."),
        "language_id": fields.Integer(required=True, description="Language ID."),
        "stdin": fields.String(default=None, description="Input for program."),
        "expected_output": fields.String(default=None, description="Expected output of program."),
        "stdout": fields.String(default=None, description="Standard output of the program after execution."),
        "status_id": fields.Integer(default=None, description="Status ID of the submission."),
        "created_at": fields.DateTime(default=None, description="Date and time when submission was created."),
        "finished_at": fields.DateTime(default=None, description="Date and time when submission was processed."),
        "time": fields.Float(default=None, description="Program's runtime in seconds."),
        "memory": fields.Float(default=None, description="Memory used by the program after execution."),
        "stderr": fields.String(default=None, description="Standard error of the program after execution."),
        "token": fields.String(default=None, description="Unique submission token."),
        "number_of_runs": fields.Integer(default=None, description="Number of runs to average time and memory."),
        "cpu_time_limit": fields.Float(default=None, description="Default runtime limit for every program."),
        "cpu_extra_time": fields.Float(default=None, description="Extra time when time limit is exceeded."),
        "wall_time_limit": fields.Float(default=None, description="Limit wall-clock time in seconds."),
        "memory_limit": fields.Float(default=None, description="Limit address space of the program."),
        "stack_limit": fields.Integer(default=None, description="Limit process stack."),
        "max_processes_and_or_threads": fields.Integer(default=None, description="Maximum number of processes/threads."),
        "enable_per_process_and_thread_time_limit": fields.Boolean(default=None, description="Use cpu_time_limit per process/thread."),
        "enable_per_process_and_thread_memory_limit": fields.Boolean(default=None, description="Use memory_limit per process/thread."),
        "max_file_size": fields.Integer(default=None, description="Limit file size created or modified."),
        "compile_output": fields.String(default=None, description="Compiler output after compilation."),
        "exit_code": fields.Integer(default=None, description="Exit code of the program."),
        "exit_signal": fields.Integer(default=None, description="Signal code received by the program before exiting."),
        "message": fields.String(default=None, description="Error message if submission status is Internal Error."),
        "wall_time": fields.Float(default=None, description="Program's wall time in seconds."),
        "compiler_options": fields.String(default=None, description="Compiler options."),
        "command_line_arguments": fields.String(default=None, description="Command line arguments for the program."),
        "redirect_stderr_to_stdout": fields.Boolean(default=None, description="Redirect stderr to stdout."),
        "callback_url": fields.String(default=None, description="Callback URL to notify when the job completes."),
        "additional_files": fields.Raw(default=None, description="Additional files associated with the program."),
        "enable_network": fields.Boolean(default=None, description="Enable network for the program."),
        "post_execution_filesystem": fields.String(default=None, description="Filesystem state after execution."),
        "status": fields.Raw(default=None, description="Submission status."),
        "language": fields.Raw(default=None, description="Programming language used."),
    }
)

token_model = compile_ns.model(
    "Token",
    {
        "token": fields.String(required=True, default="")
    }
)


@ compile_ns.route("/compile")
class createSubmissionResource(Resource):
    @ compile_ns.marshal_list_with(token_model)
    def post(self):

        data = request.get_json()
        print(data)

        return Judge0API.createSubmission(data)


@ compile_ns.route("/compile/<string:token>")
class getSubmissionResource(Resource):
    @ compile_ns.marshal_list_with(get_submission_model)
    def get(self, token):
        return Judge0API.getSubmission(token)
