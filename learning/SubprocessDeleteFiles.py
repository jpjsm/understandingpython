#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess, tempfile, string, os

    def cmdfind(path):
        '''
        Invoke the OS, using subprocess, to execute a find command.

        Arguments:
        path: The path to explore deeply; can take filesystem wildcards at leaf level.

        Return:
        rc: command execution return code
        stdout_buffer: an array of all the lines genereated to STDOUT
        stderr_buffer: an array of all the lines genereated to STDERR
        '''
        if os.path.isfile(path):
            return 0, path, ""

        if os.path.isdir(path):
            cl = ['find', path]
        else:
            cl = ['find', os.path.dirname(path), '-name', os.path.basename(path), '-mindepth', '1']

        with tempfile.TemporaryFile() as cmd_stdout, tempfile.TemporaryFile() as cmd_stderr:
            rc = subprocess.call(cl, stdout=cmd_stdout, stderr=cmd_stderr, shell=False)
            cmd_stdout.seek(0)
            stdout_buffer = [ line.strip(string.whitespace) for line in cmd_stdout.readlines() ]
            cmd_stderr.seek(0)
            stderr_buffer = [ line.strip(string.whitespace) for line in cmd_stderr.readlines() ]
        return rc, stdout_buffer, stderr_buffer

    def delete_files(path, exit_on_error = True):
        result = {'status':'200'}
        sc, stdout_buffer, stderr_buffer = PassthroughProxyApi.cmdfind(path)
        if exit_on_error and len(stderr_buffer) > 0:
            result['message'] = string.join(stderr_buffer, ', ')
            result['status'] = 400
            return result, result['status']
        
        result['deleted'] = []
        try:
            for f in sorted(stdout_buffer, key=lambda l: len(l), reverse=True):
                if os.path.isfile(f):
                    os.remove(f)
                elif os.path.isdir(f):
                    os.removedirs(f)
                elif os.path.islink(f):
                    os.unlink(f)
                else:
                    result['message'] = "Unknown object type: {}".format(f)
                    result['status'] = 400
                    return result, result['status']

                result['deleted'].append(f)

        except OSError as e:
            result['status'] = '500'
            result['message'] = e.strerror + "[" + str(e.errno) + "]: 'Server Certs Location' " + e.filename
            return result, int(result['status'])

        return stdout_buffer, int(result['status'])


print "-"*72
# for f in cmdfind('/Users/jjofre/virtualenvs/learning/python/testfiles/*')[1]
for f in delete_files('/Users/jjofre/virtualenvs/learning/python/testfiles/*'):
    print "\t{}".format(f)
print "-"*72
