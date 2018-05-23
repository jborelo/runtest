import os
import sys
import subprocess


# ------------------------------------------------------
def callScript(params):
    script = os.path.join(r'test/myapp.py')
    command = "python"
    cmd = [command, script, params]
    print(cmd)
    # out_bytes = subprocess.check_output(cmd, stderr=subprocess.STDOUT)



    pipes = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    std_out, std_err = pipes.communicate()

    if pipes.returncode != 0:
        # an error happened!
        err_msg = "%s. Code: %s" % (std_err.decode('utf_8').strip(), pipes.returncode)
        print(err_msg)
        return "Execution of your analytical function failed "


    out_text = std_out.decode('utf_8')
    print(out_text)

    return out_text


if __name__ == "__main__":
    params = ""
    if len(sys.argv)>1:
        params =  sys.argv[1]

    callScript(params)

