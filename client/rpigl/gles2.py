
import ctypes
from .load_gles import load_gl_proc, GLError

_glCullFace = load_gl_proc(b"glCullFace", None, (ctypes.c_uint,))
def glCullFace(mode):
    return _glCullFace(mode)
_glFrontFace = load_gl_proc(b"glFrontFace", None, (ctypes.c_uint,))
def glFrontFace(mode):
    return _glFrontFace(mode)
_glHint = load_gl_proc(b"glHint", None, (ctypes.c_uint, ctypes.c_uint,))
def glHint(target, mode):
    return _glHint(target, mode)
_glLineWidth = load_gl_proc(b"glLineWidth", None, (ctypes.c_float,))
def glLineWidth(width):
    return _glLineWidth(width)
_glPointSize = load_gl_proc(b"glPointSize", None, (ctypes.c_float,))
def glPointSize(size):
    return _glPointSize(size)
_glScissor = load_gl_proc(b"glScissor", None, (ctypes.c_int, ctypes.c_int, ctypes.c_size_t, ctypes.c_size_t,))
def glScissor(x, y, width, height):
    return _glScissor(x, y, width, height)
_glTexParameterf = load_gl_proc(b"glTexParameterf", None, (ctypes.c_uint, ctypes.c_uint, ctypes.c_float,))
def glTexParameterf(target, pname, param):
    return _glTexParameterf(target, pname, param)
_glTexParameterfv = load_gl_proc(b"glTexParameterfv", None, (ctypes.c_uint, ctypes.c_uint, ctypes.POINTER(ctypes.c_float),))
def glTexParameterfv(target, pname, params):
    return _glTexParameterfv(target, pname, params)
_glTexParameteri = load_gl_proc(b"glTexParameteri", None, (ctypes.c_uint, ctypes.c_uint, ctypes.c_long,))
def glTexParameteri(target, pname, param):
    return _glTexParameteri(target, pname, param)
_glTexParameteriv = load_gl_proc(b"glTexParameteriv", None, (ctypes.c_uint, ctypes.c_uint, ctypes.POINTER(ctypes.c_long),))
def glTexParameteriv(target, pname, params):
    return _glTexParameteriv(target, pname, params)
_glTexImage2D = load_gl_proc(b"glTexImage2D", None, (ctypes.c_uint, ctypes.c_long, ctypes.c_int, ctypes.c_size_t, ctypes.c_size_t, ctypes.c_long, ctypes.c_uint, ctypes.c_uint, ctypes.c_void_p,))
def glTexImage2D(target, level, internalformat, width, height, border, format, type, pixels):
    return _glTexImage2D(target, level, internalformat, width, height, border, format, type, pixels)
_glClear = load_gl_proc(b"glClear", None, (ctypes.c_uint,))
def glClear(mask):
    return _glClear(mask)
_glClearColor = load_gl_proc(b"glClearColor", None, (ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float,))
def glClearColor(red, green, blue, alpha):
    return _glClearColor(red, green, blue, alpha)
_glClearStencil = load_gl_proc(b"glClearStencil", None, (ctypes.c_int,))
def glClearStencil(s):
    return _glClearStencil(s)
_glStencilMask = load_gl_proc(b"glStencilMask", None, (ctypes.c_uint,))
def glStencilMask(mask):
    return _glStencilMask(mask)
_glColorMask = load_gl_proc(b"glColorMask", None, (ctypes.c_ubyte, ctypes.c_ubyte, ctypes.c_ubyte, ctypes.c_ubyte,))
def glColorMask(red, green, blue, alpha):
    return _glColorMask(red, green, blue, alpha)
_glDepthMask = load_gl_proc(b"glDepthMask", None, (ctypes.c_ubyte,))
def glDepthMask(flag):
    return _glDepthMask(flag)
_glDisable = load_gl_proc(b"glDisable", None, (ctypes.c_uint,))
def glDisable(cap):
    return _glDisable(cap)
_glEnable = load_gl_proc(b"glEnable", None, (ctypes.c_uint,))
def glEnable(cap):
    return _glEnable(cap)
_glFinish = load_gl_proc(b"glFinish", None, ())
def glFinish():
    return _glFinish()
_glFlush = load_gl_proc(b"glFlush", None, ())
def glFlush():
    return _glFlush()
_glBlendFunc = load_gl_proc(b"glBlendFunc", None, (ctypes.c_uint, ctypes.c_uint,))
def glBlendFunc(sfactor, dfactor):
    return _glBlendFunc(sfactor, dfactor)
_glLogicOp = load_gl_proc(b"glLogicOp", None, (ctypes.c_uint,))
def glLogicOp(opcode):
    return _glLogicOp(opcode)
_glStencilFunc = load_gl_proc(b"glStencilFunc", None, (ctypes.c_uint, ctypes.c_int, ctypes.c_uint,))
def glStencilFunc(func, ref, mask):
    return _glStencilFunc(func, ref, mask)
_glStencilOp = load_gl_proc(b"glStencilOp", None, (ctypes.c_uint, ctypes.c_uint, ctypes.c_uint,))
def glStencilOp(fail, zfail, zpass):
    return _glStencilOp(fail, zfail, zpass)
_glDepthFunc = load_gl_proc(b"glDepthFunc", None, (ctypes.c_uint,))
def glDepthFunc(func):
    return _glDepthFunc(func)
_glPixelStorei = load_gl_proc(b"glPixelStorei", None, (ctypes.c_uint, ctypes.c_long,))
def glPixelStorei(pname, param):
    return _glPixelStorei(pname, param)
_glReadPixels = load_gl_proc(b"glReadPixels", None, (ctypes.c_int, ctypes.c_int, ctypes.c_size_t, ctypes.c_size_t, ctypes.c_uint, ctypes.c_uint, ctypes.c_void_p,))
def glReadPixels(x, y, width, height, format, type, pixels):
    return _glReadPixels(x, y, width, height, format, type, pixels)
_glGetBooleanv = load_gl_proc(b"glGetBooleanv", None, (ctypes.c_uint, ctypes.POINTER(ctypes.c_ubyte),))
def glGetBooleanv(pname, params):
    return _glGetBooleanv(pname, params)
_glGetError = load_gl_proc(b"glGetError", ctypes.c_uint, ())
def glGetError():
    return _glGetError()
_glGetFloatv = load_gl_proc(b"glGetFloatv", None, (ctypes.c_uint, ctypes.POINTER(ctypes.c_float),))
def glGetFloatv(pname, params):
    return _glGetFloatv(pname, params)
_glGetIntegerv = load_gl_proc(b"glGetIntegerv", None, (ctypes.c_uint, ctypes.POINTER(ctypes.c_int32),))
def glGetIntegerv(pname, params):
    return _glGetIntegerv(pname, params)
_glGetString = load_gl_proc(b"glGetString", ctypes.c_char_p, (ctypes.c_uint,))
def glGetString(name):
    return _glGetString(name)
_glGetTexParameterfv = load_gl_proc(b"glGetTexParameterfv", None, (ctypes.c_uint, ctypes.c_uint, ctypes.POINTER(ctypes.c_float),))
def glGetTexParameterfv(target, pname, params):
    return _glGetTexParameterfv(target, pname, params)
_glGetTexParameteriv = load_gl_proc(b"glGetTexParameteriv", None, (ctypes.c_uint, ctypes.c_uint, ctypes.POINTER(ctypes.c_int32),))
def glGetTexParameteriv(target, pname, params):
    return _glGetTexParameteriv(target, pname, params)
_glIsEnabled = load_gl_proc(b"glIsEnabled", ctypes.c_ubyte, (ctypes.c_uint,))
def glIsEnabled(cap):
    return _glIsEnabled(cap)
_glViewport = load_gl_proc(b"glViewport", None, (ctypes.c_int, ctypes.c_int, ctypes.c_size_t, ctypes.c_size_t,))
def glViewport(x, y, width, height):
    return _glViewport(x, y, width, height)
_glDrawArrays = load_gl_proc(b"glDrawArrays", None, (ctypes.c_uint, ctypes.c_int32, ctypes.c_size_t,))
def glDrawArrays(mode, first, count):
    return _glDrawArrays(mode, first, count)
_glDrawElements = load_gl_proc(b"glDrawElements", None, (ctypes.c_uint, ctypes.c_size_t, ctypes.c_uint, ctypes.c_void_p,))
def glDrawElements(mode, count, type, indices):
    return _glDrawElements(mode, count, type, indices)
_glGetPointerv = load_gl_proc(b"glGetPointerv", None, (ctypes.c_uint, ctypes.POINTER(ctypes.c_void_p),))
def glGetPointerv(pname, params):
    return _glGetPointerv(pname, params)
_glPolygonOffset = load_gl_proc(b"glPolygonOffset", None, (ctypes.c_float, ctypes.c_float,))
def glPolygonOffset(factor, units):
    return _glPolygonOffset(factor, units)
_glCopyTexImage2D = load_gl_proc(b"glCopyTexImage2D", None, (ctypes.c_uint, ctypes.c_long, ctypes.c_uint, ctypes.c_int, ctypes.c_int, ctypes.c_size_t, ctypes.c_size_t, ctypes.c_long,))
def glCopyTexImage2D(target, level, internalformat, x, y, width, height, border):
    return _glCopyTexImage2D(target, level, internalformat, x, y, width, height, border)
_glCopyTexSubImage2D = load_gl_proc(b"glCopyTexSubImage2D", None, (ctypes.c_uint, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_int, ctypes.c_int, ctypes.c_size_t, ctypes.c_size_t,))
def glCopyTexSubImage2D(target, level, xoffset, yoffset, x, y, width, height):
    return _glCopyTexSubImage2D(target, level, xoffset, yoffset, x, y, width, height)
_glTexSubImage2D = load_gl_proc(b"glTexSubImage2D", None, (ctypes.c_uint, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_size_t, ctypes.c_size_t, ctypes.c_uint, ctypes.c_uint, ctypes.c_void_p,))
def glTexSubImage2D(target, level, xoffset, yoffset, width, height, format, type, pixels):
    return _glTexSubImage2D(target, level, xoffset, yoffset, width, height, format, type, pixels)
_glBindTexture = load_gl_proc(b"glBindTexture", None, (ctypes.c_uint, ctypes.c_uint,))
def glBindTexture(target, texture):
    return _glBindTexture(target, texture)
_glDeleteTextures = load_gl_proc(b"glDeleteTextures", None, (ctypes.c_size_t, ctypes.POINTER(ctypes.c_uint),))
def glDeleteTextures(n, textures):
    return _glDeleteTextures(n, textures)
_glGenTextures = load_gl_proc(b"glGenTextures", None, (ctypes.c_size_t, ctypes.POINTER(ctypes.c_uint),))
def glGenTextures(n, textures):
    return _glGenTextures(n, textures)
_glIsTexture = load_gl_proc(b"glIsTexture", ctypes.c_ubyte, (ctypes.c_uint,))
def glIsTexture(texture):
    return _glIsTexture(texture)
_glBlendColor = load_gl_proc(b"glBlendColor", None, (ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float,))
def glBlendColor(red, green, blue, alpha):
    return _glBlendColor(red, green, blue, alpha)
_glBlendEquation = load_gl_proc(b"glBlendEquation", None, (ctypes.c_uint,))
def glBlendEquation(mode):
    return _glBlendEquation(mode)
_glActiveTexture = load_gl_proc(b"glActiveTexture", None, (ctypes.c_uint,))
def glActiveTexture(texture):
    return _glActiveTexture(texture)
_glSampleCoverage = load_gl_proc(b"glSampleCoverage", None, (ctypes.c_float, ctypes.c_ubyte,))
def glSampleCoverage(value, invert):
    return _glSampleCoverage(value, invert)
_glCompressedTexImage2D = load_gl_proc(b"glCompressedTexImage2D", None, (ctypes.c_uint, ctypes.c_long, ctypes.c_uint, ctypes.c_size_t, ctypes.c_size_t, ctypes.c_long, ctypes.c_size_t, ctypes.c_void_p,))
def glCompressedTexImage2D(target, level, internalformat, width, height, border, imageSize, data):
    return _glCompressedTexImage2D(target, level, internalformat, width, height, border, imageSize, data)
_glCompressedTexSubImage2D = load_gl_proc(b"glCompressedTexSubImage2D", None, (ctypes.c_uint, ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_size_t, ctypes.c_size_t, ctypes.c_uint, ctypes.c_size_t, ctypes.c_void_p,))
def glCompressedTexSubImage2D(target, level, xoffset, yoffset, width, height, format, imageSize, data):
    return _glCompressedTexSubImage2D(target, level, xoffset, yoffset, width, height, format, imageSize, data)
_glBlendFuncSeparate = load_gl_proc(b"glBlendFuncSeparate", None, (ctypes.c_uint, ctypes.c_uint, ctypes.c_uint, ctypes.c_uint,))
def glBlendFuncSeparate(sfactorRGB, dfactorRGB, sfactorAlpha, dfactorAlpha):
    return _glBlendFuncSeparate(sfactorRGB, dfactorRGB, sfactorAlpha, dfactorAlpha)
_glPointParameterf = load_gl_proc(b"glPointParameterf", None, (ctypes.c_uint, ctypes.c_float,))
def glPointParameterf(pname, param):
    return _glPointParameterf(pname, param)
_glPointParameterfv = load_gl_proc(b"glPointParameterfv", None, (ctypes.c_uint, ctypes.POINTER(ctypes.c_float),))
def glPointParameterfv(pname, params):
    return _glPointParameterfv(pname, params)
_glBindBuffer = load_gl_proc(b"glBindBuffer", None, (ctypes.c_uint, ctypes.c_uint32,))
def glBindBuffer(target, buffer):
    return _glBindBuffer(target, buffer)
_glDeleteBuffers = load_gl_proc(b"glDeleteBuffers", None, (ctypes.c_size_t, ctypes.POINTER(ctypes.c_ulong),))
def glDeleteBuffers(n, buffers):
    return _glDeleteBuffers(n, buffers)
_glGenBuffers = load_gl_proc(b"glGenBuffers", None, (ctypes.c_size_t, ctypes.POINTER(ctypes.c_uint32),))
def glGenBuffers(n, buffers):
    return _glGenBuffers(n, buffers)
_glIsBuffer = load_gl_proc(b"glIsBuffer", ctypes.c_ubyte, (ctypes.c_uint32,))
def glIsBuffer(buffer):
    return _glIsBuffer(buffer)
_glBufferData = load_gl_proc(b"glBufferData", None, (ctypes.c_uint, ctypes.c_ssize_t, ctypes.c_void_p, ctypes.c_uint,))
def glBufferData(target, size, data, usage):
    return _glBufferData(target, size, data, usage)
_glBufferSubData = load_gl_proc(b"glBufferSubData", None, (ctypes.c_uint, ctypes.c_size_t, ctypes.c_ssize_t, ctypes.c_void_p,))
def glBufferSubData(target, offset, size, data):
    return _glBufferSubData(target, offset, size, data)
_glGetBufferParameteriv = load_gl_proc(b"glGetBufferParameteriv", None, (ctypes.c_uint, ctypes.c_uint, ctypes.POINTER(ctypes.c_int32),))
def glGetBufferParameteriv(target, pname, params):
    return _glGetBufferParameteriv(target, pname, params)
_glBlendEquationSeparate = load_gl_proc(b"glBlendEquationSeparate", None, (ctypes.c_uint, ctypes.c_uint,))
def glBlendEquationSeparate(modeRGB, modeAlpha):
    return _glBlendEquationSeparate(modeRGB, modeAlpha)
_glStencilOpSeparate = load_gl_proc(b"glStencilOpSeparate", None, (ctypes.c_uint, ctypes.c_uint, ctypes.c_uint, ctypes.c_uint,))
def glStencilOpSeparate(face, sfail, dpfail, dppass):
    return _glStencilOpSeparate(face, sfail, dpfail, dppass)
_glStencilFuncSeparate = load_gl_proc(b"glStencilFuncSeparate", None, (ctypes.c_uint, ctypes.c_uint, ctypes.c_int, ctypes.c_uint,))
def glStencilFuncSeparate(face, func, ref, mask):
    return _glStencilFuncSeparate(face, func, ref, mask)
_glStencilMaskSeparate = load_gl_proc(b"glStencilMaskSeparate", None, (ctypes.c_uint, ctypes.c_uint,))
def glStencilMaskSeparate(face, mask):
    return _glStencilMaskSeparate(face, mask)
_glAttachShader = load_gl_proc(b"glAttachShader", None, (ctypes.c_uint32, ctypes.c_uint32,))
def glAttachShader(program, shader):
    return _glAttachShader(program, shader)
_glBindAttribLocation = load_gl_proc(b"glBindAttribLocation", None, (ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(ctypes.c_char),))
def glBindAttribLocation(program, index, name):
    return _glBindAttribLocation(program, index, name)
_glCompileShader = load_gl_proc(b"glCompileShader", None, (ctypes.c_uint32,))
def glCompileShader(shader):
    return _glCompileShader(shader)
_glCreateProgram = load_gl_proc(b"glCreateProgram", ctypes.c_uint32, ())
def glCreateProgram():
    return _glCreateProgram()
_glCreateShader = load_gl_proc(b"glCreateShader", ctypes.c_uint32, (ctypes.c_uint,))
def glCreateShader(type):
    return _glCreateShader(type)
_glDeleteProgram = load_gl_proc(b"glDeleteProgram", None, (ctypes.c_uint32,))
def glDeleteProgram(program):
    return _glDeleteProgram(program)
_glDeleteShader = load_gl_proc(b"glDeleteShader", None, (ctypes.c_uint32,))
def glDeleteShader(shader):
    return _glDeleteShader(shader)
_glDetachShader = load_gl_proc(b"glDetachShader", None, (ctypes.c_uint32, ctypes.c_uint32,))
def glDetachShader(program, shader):
    return _glDetachShader(program, shader)
_glDisableVertexAttribArray = load_gl_proc(b"glDisableVertexAttribArray", None, (ctypes.c_uint32,))
def glDisableVertexAttribArray(index):
    return _glDisableVertexAttribArray(index)
_glEnableVertexAttribArray = load_gl_proc(b"glEnableVertexAttribArray", None, (ctypes.c_uint32,))
def glEnableVertexAttribArray(index):
    return _glEnableVertexAttribArray(index)
_glGetActiveAttrib = load_gl_proc(b"glGetActiveAttrib", None, (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_size_t, ctypes.POINTER(ctypes.c_size_t), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_uint), ctypes.POINTER(ctypes.c_char),))
def glGetActiveAttrib(program, index, bufSize, length, size, type, name):
    return _glGetActiveAttrib(program, index, bufSize, length, size, type, name)
_glGetActiveUniform = load_gl_proc(b"glGetActiveUniform", None, (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_size_t, ctypes.POINTER(ctypes.c_size_t), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_uint), ctypes.POINTER(ctypes.c_char),))
def glGetActiveUniform(program, index, bufSize, length, size, type, name):
    return _glGetActiveUniform(program, index, bufSize, length, size, type, name)
_glGetAttachedShaders = load_gl_proc(b"glGetAttachedShaders", None, (ctypes.c_uint32, ctypes.c_size_t, ctypes.POINTER(ctypes.c_size_t), ctypes.POINTER(ctypes.c_uint32),))
def glGetAttachedShaders(program, maxCount, count, obj):
    return _glGetAttachedShaders(program, maxCount, count, obj)
_glGetAttribLocation = load_gl_proc(b"glGetAttribLocation", ctypes.c_int32, (ctypes.c_uint32, ctypes.POINTER(ctypes.c_char),))
def glGetAttribLocation(program, name):
    return _glGetAttribLocation(program, name)
_glGetProgramiv = load_gl_proc(b"glGetProgramiv", None, (ctypes.c_uint32, ctypes.c_uint, ctypes.POINTER(ctypes.c_int32),))
def glGetProgramiv(program, pname, params):
    return _glGetProgramiv(program, pname, params)
_glGetProgramInfoLog = load_gl_proc(b"glGetProgramInfoLog", None, (ctypes.c_uint32, ctypes.c_size_t, ctypes.POINTER(ctypes.c_size_t), ctypes.POINTER(ctypes.c_char),))
def glGetProgramInfoLog(program, bufSize, length, infoLog):
    return _glGetProgramInfoLog(program, bufSize, length, infoLog)
_glGetShaderiv = load_gl_proc(b"glGetShaderiv", None, (ctypes.c_uint32, ctypes.c_uint, ctypes.POINTER(ctypes.c_int32),))
def glGetShaderiv(shader, pname, params):
    return _glGetShaderiv(shader, pname, params)
_glGetShaderInfoLog = load_gl_proc(b"glGetShaderInfoLog", None, (ctypes.c_uint32, ctypes.c_size_t, ctypes.POINTER(ctypes.c_size_t), ctypes.POINTER(ctypes.c_char),))
def glGetShaderInfoLog(shader, bufSize, length, infoLog):
    return _glGetShaderInfoLog(shader, bufSize, length, infoLog)
_glGetShaderSource = load_gl_proc(b"glGetShaderSource", None, (ctypes.c_uint32, ctypes.c_size_t, ctypes.POINTER(ctypes.c_size_t), ctypes.POINTER(ctypes.c_char),))
def glGetShaderSource(shader, bufSize, length, source):
    return _glGetShaderSource(shader, bufSize, length, source)
_glGetUniformLocation = load_gl_proc(b"glGetUniformLocation", ctypes.c_int32, (ctypes.c_uint32, ctypes.POINTER(ctypes.c_char),))
def glGetUniformLocation(program, name):
    return _glGetUniformLocation(program, name)
_glGetUniformfv = load_gl_proc(b"glGetUniformfv", None, (ctypes.c_uint32, ctypes.c_int32, ctypes.POINTER(ctypes.c_float),))
def glGetUniformfv(program, location, params):
    return _glGetUniformfv(program, location, params)
_glGetUniformiv = load_gl_proc(b"glGetUniformiv", None, (ctypes.c_uint32, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32),))
def glGetUniformiv(program, location, params):
    return _glGetUniformiv(program, location, params)
_glGetVertexAttribfv = load_gl_proc(b"glGetVertexAttribfv", None, (ctypes.c_uint32, ctypes.c_uint, ctypes.POINTER(ctypes.c_float),))
def glGetVertexAttribfv(index, pname, params):
    return _glGetVertexAttribfv(index, pname, params)
_glGetVertexAttribiv = load_gl_proc(b"glGetVertexAttribiv", None, (ctypes.c_uint32, ctypes.c_uint, ctypes.POINTER(ctypes.c_int32),))
def glGetVertexAttribiv(index, pname, params):
    return _glGetVertexAttribiv(index, pname, params)
_glGetVertexAttribPointerv = load_gl_proc(b"glGetVertexAttribPointerv", None, (ctypes.c_uint32, ctypes.c_uint, ctypes.POINTER(ctypes.c_void_p),))
def glGetVertexAttribPointerv(index, pname, pointer):
    return _glGetVertexAttribPointerv(index, pname, pointer)
_glIsProgram = load_gl_proc(b"glIsProgram", ctypes.c_ubyte, (ctypes.c_uint32,))
def glIsProgram(program):
    return _glIsProgram(program)
_glIsShader = load_gl_proc(b"glIsShader", ctypes.c_ubyte, (ctypes.c_uint32,))
def glIsShader(shader):
    return _glIsShader(shader)
_glLinkProgram = load_gl_proc(b"glLinkProgram", None, (ctypes.c_uint32,))
def glLinkProgram(program):
    return _glLinkProgram(program)
_glShaderSource = load_gl_proc(b"glShaderSource", None, (ctypes.c_uint32, ctypes.c_size_t, ctypes.POINTER(ctypes.c_char_p), ctypes.POINTER(ctypes.c_int32),))
def glShaderSource(shader, count, string, length):
    return _glShaderSource(shader, count, string, length)
_glUseProgram = load_gl_proc(b"glUseProgram", None, (ctypes.c_uint32,))
def glUseProgram(program):
    return _glUseProgram(program)
_glUniform1f = load_gl_proc(b"glUniform1f", None, (ctypes.c_int32, ctypes.c_float,))
def glUniform1f(location, v0):
    return _glUniform1f(location, v0)
_glUniform2f = load_gl_proc(b"glUniform2f", None, (ctypes.c_int32, ctypes.c_float, ctypes.c_float,))
def glUniform2f(location, v0, v1):
    return _glUniform2f(location, v0, v1)
_glUniform3f = load_gl_proc(b"glUniform3f", None, (ctypes.c_int32, ctypes.c_float, ctypes.c_float, ctypes.c_float,))
def glUniform3f(location, v0, v1, v2):
    return _glUniform3f(location, v0, v1, v2)
_glUniform4f = load_gl_proc(b"glUniform4f", None, (ctypes.c_int32, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float,))
def glUniform4f(location, v0, v1, v2, v3):
    return _glUniform4f(location, v0, v1, v2, v3)
_glUniform1i = load_gl_proc(b"glUniform1i", None, (ctypes.c_int32, ctypes.c_int32,))
def glUniform1i(location, v0):
    return _glUniform1i(location, v0)
_glUniform2i = load_gl_proc(b"glUniform2i", None, (ctypes.c_int32, ctypes.c_int32, ctypes.c_int32,))
def glUniform2i(location, v0, v1):
    return _glUniform2i(location, v0, v1)
_glUniform3i = load_gl_proc(b"glUniform3i", None, (ctypes.c_int32, ctypes.c_int32, ctypes.c_int32, ctypes.c_int32,))
def glUniform3i(location, v0, v1, v2):
    return _glUniform3i(location, v0, v1, v2)
_glUniform4i = load_gl_proc(b"glUniform4i", None, (ctypes.c_int32, ctypes.c_int32, ctypes.c_int32, ctypes.c_int32, ctypes.c_int32,))
def glUniform4i(location, v0, v1, v2, v3):
    return _glUniform4i(location, v0, v1, v2, v3)
_glUniform1fv = load_gl_proc(b"glUniform1fv", None, (ctypes.c_int32, ctypes.c_size_t, ctypes.POINTER(ctypes.c_float),))
def glUniform1fv(location, count, value):
    return _glUniform1fv(location, count, value)
_glUniform2fv = load_gl_proc(b"glUniform2fv", None, (ctypes.c_int32, ctypes.c_size_t, ctypes.POINTER(ctypes.c_float),))
def glUniform2fv(location, count, value):
    return _glUniform2fv(location, count, value)
_glUniform3fv = load_gl_proc(b"glUniform3fv", None, (ctypes.c_int32, ctypes.c_size_t, ctypes.POINTER(ctypes.c_float),))
def glUniform3fv(location, count, value):
    return _glUniform3fv(location, count, value)
_glUniform4fv = load_gl_proc(b"glUniform4fv", None, (ctypes.c_int32, ctypes.c_size_t, ctypes.POINTER(ctypes.c_float),))
def glUniform4fv(location, count, value):
    return _glUniform4fv(location, count, value)
_glUniform1iv = load_gl_proc(b"glUniform1iv", None, (ctypes.c_int32, ctypes.c_size_t, ctypes.POINTER(ctypes.c_int32),))
def glUniform1iv(location, count, value):
    return _glUniform1iv(location, count, value)
_glUniform2iv = load_gl_proc(b"glUniform2iv", None, (ctypes.c_int32, ctypes.c_size_t, ctypes.POINTER(ctypes.c_int32),))
def glUniform2iv(location, count, value):
    return _glUniform2iv(location, count, value)
_glUniform3iv = load_gl_proc(b"glUniform3iv", None, (ctypes.c_int32, ctypes.c_size_t, ctypes.POINTER(ctypes.c_int32),))
def glUniform3iv(location, count, value):
    return _glUniform3iv(location, count, value)
_glUniform4iv = load_gl_proc(b"glUniform4iv", None, (ctypes.c_int32, ctypes.c_size_t, ctypes.POINTER(ctypes.c_int32),))
def glUniform4iv(location, count, value):
    return _glUniform4iv(location, count, value)
_glUniformMatrix2fv = load_gl_proc(b"glUniformMatrix2fv", None, (ctypes.c_int32, ctypes.c_size_t, ctypes.c_ubyte, ctypes.POINTER(ctypes.c_float),))
def glUniformMatrix2fv(location, count, transpose, value):
    return _glUniformMatrix2fv(location, count, transpose, value)
_glUniformMatrix3fv = load_gl_proc(b"glUniformMatrix3fv", None, (ctypes.c_int32, ctypes.c_size_t, ctypes.c_ubyte, ctypes.POINTER(ctypes.c_float),))
def glUniformMatrix3fv(location, count, transpose, value):
    return _glUniformMatrix3fv(location, count, transpose, value)
_glUniformMatrix4fv = load_gl_proc(b"glUniformMatrix4fv", None, (ctypes.c_int32, ctypes.c_size_t, ctypes.c_ubyte, ctypes.POINTER(ctypes.c_float),))
def glUniformMatrix4fv(location, count, transpose, value):
    return _glUniformMatrix4fv(location, count, transpose, value)
_glValidateProgram = load_gl_proc(b"glValidateProgram", None, (ctypes.c_uint32,))
def glValidateProgram(program):
    return _glValidateProgram(program)
_glVertexAttribPointer = load_gl_proc(b"glVertexAttribPointer", None, (ctypes.c_uint32, ctypes.c_int32, ctypes.c_uint, ctypes.c_ubyte, ctypes.c_size_t, ctypes.c_void_p,))
def glVertexAttribPointer(index, size, type, normalized, stride, pointer):
    return _glVertexAttribPointer(index, size, type, normalized, stride, pointer)
_glIsRenderbuffer = load_gl_proc(b"glIsRenderbuffer", ctypes.c_ubyte, (ctypes.c_uint32,))
def glIsRenderbuffer(renderbuffer):
    return _glIsRenderbuffer(renderbuffer)
_glBindRenderbuffer = load_gl_proc(b"glBindRenderbuffer", None, (ctypes.c_uint, ctypes.c_uint32,))
def glBindRenderbuffer(target, renderbuffer):
    return _glBindRenderbuffer(target, renderbuffer)
_glDeleteRenderbuffers = load_gl_proc(b"glDeleteRenderbuffers", None, (ctypes.c_size_t, ctypes.POINTER(ctypes.c_uint32),))
def glDeleteRenderbuffers(n, renderbuffers):
    return _glDeleteRenderbuffers(n, renderbuffers)
_glGenRenderbuffers = load_gl_proc(b"glGenRenderbuffers", None, (ctypes.c_size_t, ctypes.POINTER(ctypes.c_uint32),))
def glGenRenderbuffers(n, renderbuffers):
    return _glGenRenderbuffers(n, renderbuffers)
_glRenderbufferStorage = load_gl_proc(b"glRenderbufferStorage", None, (ctypes.c_uint, ctypes.c_uint, ctypes.c_size_t, ctypes.c_size_t,))
def glRenderbufferStorage(target, internalformat, width, height):
    return _glRenderbufferStorage(target, internalformat, width, height)
_glGetRenderbufferParameteriv = load_gl_proc(b"glGetRenderbufferParameteriv", None, (ctypes.c_uint, ctypes.c_uint, ctypes.POINTER(ctypes.c_int32),))
def glGetRenderbufferParameteriv(target, pname, params):
    return _glGetRenderbufferParameteriv(target, pname, params)
_glIsFramebuffer = load_gl_proc(b"glIsFramebuffer", ctypes.c_ubyte, (ctypes.c_uint32,))
def glIsFramebuffer(framebuffer):
    return _glIsFramebuffer(framebuffer)
_glBindFramebuffer = load_gl_proc(b"glBindFramebuffer", None, (ctypes.c_uint, ctypes.c_uint32,))
def glBindFramebuffer(target, framebuffer):
    return _glBindFramebuffer(target, framebuffer)
_glDeleteFramebuffers = load_gl_proc(b"glDeleteFramebuffers", None, (ctypes.c_size_t, ctypes.POINTER(ctypes.c_uint32),))
def glDeleteFramebuffers(n, framebuffers):
    return _glDeleteFramebuffers(n, framebuffers)
_glGenFramebuffers = load_gl_proc(b"glGenFramebuffers", None, (ctypes.c_size_t, ctypes.POINTER(ctypes.c_uint32),))
def glGenFramebuffers(n, framebuffers):
    return _glGenFramebuffers(n, framebuffers)
_glCheckFramebufferStatus = load_gl_proc(b"glCheckFramebufferStatus", ctypes.c_uint, (ctypes.c_uint,))
def glCheckFramebufferStatus(target):
    return _glCheckFramebufferStatus(target)
_glFramebufferTexture2D = load_gl_proc(b"glFramebufferTexture2D", None, (ctypes.c_uint, ctypes.c_uint, ctypes.c_uint, ctypes.c_uint32, ctypes.c_int32,))
def glFramebufferTexture2D(target, attachment, textarget, texture, level):
    return _glFramebufferTexture2D(target, attachment, textarget, texture, level)
_glFramebufferRenderbuffer = load_gl_proc(b"glFramebufferRenderbuffer", None, (ctypes.c_uint, ctypes.c_uint, ctypes.c_uint, ctypes.c_uint32,))
def glFramebufferRenderbuffer(target, attachment, renderbuffertarget, renderbuffer):
    return _glFramebufferRenderbuffer(target, attachment, renderbuffertarget, renderbuffer)
_glGetFramebufferAttachmentParameteriv = load_gl_proc(b"glGetFramebufferAttachmentParameteriv", None, (ctypes.c_uint, ctypes.c_uint, ctypes.c_uint, ctypes.POINTER(ctypes.c_int32),))
def glGetFramebufferAttachmentParameteriv(target, attachment, pname, params):
    return _glGetFramebufferAttachmentParameteriv(target, attachment, pname, params)
_glGenerateMipmap = load_gl_proc(b"glGenerateMipmap", None, (ctypes.c_uint,))
def glGenerateMipmap(target):
    return _glGenerateMipmap(target)
_glReleaseShaderCompiler = load_gl_proc(b"glReleaseShaderCompiler", None, ())
def glReleaseShaderCompiler():
    return _glReleaseShaderCompiler()
_glShaderBinary = load_gl_proc(b"glShaderBinary", None, (ctypes.c_size_t, ctypes.POINTER(ctypes.c_uint32), ctypes.c_uint, ctypes.c_void_p, ctypes.c_size_t,))
def glShaderBinary(count, shaders, binaryformat, binary, length):
    return _glShaderBinary(count, shaders, binaryformat, binary, length)
_glGetShaderPrecisionFormat = load_gl_proc(b"glGetShaderPrecisionFormat", None, (ctypes.c_uint, ctypes.c_uint, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32),))
def glGetShaderPrecisionFormat(shadertype, precisiontype, range, precision):
    return _glGetShaderPrecisionFormat(shadertype, precisiontype, range, precision)
_glDepthRangef = load_gl_proc(b"glDepthRangef", None, (ctypes.c_float, ctypes.c_float,))
def glDepthRangef(n, f):
    return _glDepthRangef(n, f)
_glClearDepthf = load_gl_proc(b"glClearDepthf", None, (ctypes.c_float,))
def glClearDepthf(d):
    return _glClearDepthf(d)
GL_VERSION_1_1 = 1
GL_VERSION_1_2 = 1
GL_VERSION_1_3 = 1
GL_VERSION_1_4 = 1
GL_VERSION_1_5 = 1
GL_VERSION_2_0 = 1
GL_VERSION_2_1 = 1
GL_VERSION_3_0 = 1
GL_VERSION_3_1 = 1
GL_VERSION_3_2 = 1
GL_CURRENT_BIT = 0x00000001
GL_POINT_BIT = 0x00000002
GL_LINE_BIT = 0x00000004
GL_POLYGON_BIT = 0x00000008
GL_POLYGON_STIPPLE_BIT = 0x00000010
GL_PIXEL_MODE_BIT = 0x00000020
GL_LIGHTING_BIT = 0x00000040
GL_FOG_BIT = 0x00000080
GL_DEPTH_BUFFER_BIT = 0x00000100
GL_ACCUM_BUFFER_BIT = 0x00000200
GL_STENCIL_BUFFER_BIT = 0x00000400
GL_VIEWPORT_BIT = 0x00000800
GL_TRANSFORM_BIT = 0x00001000
GL_ENABLE_BIT = 0x00002000
GL_COLOR_BUFFER_BIT = 0x00004000
GL_HINT_BIT = 0x00008000
GL_EVAL_BIT = 0x00010000
GL_LIST_BIT = 0x00020000
GL_TEXTURE_BIT = 0x00040000
GL_SCISSOR_BIT = 0x00080000
GL_ALL_ATTRIB_BITS = 0xFFFFFFFF
GL_MULTISAMPLE_BIT = 0x20000000
GL_CLIENT_PIXEL_STORE_BIT = 0x00000001
GL_CLIENT_VERTEX_ARRAY_BIT = 0x00000002
GL_CLIENT_ALL_ATTRIB_BITS = 0xFFFFFFFF
GL_MAP_READ_BIT = 0x0001
GL_MAP_WRITE_BIT = 0x0002
GL_MAP_INVALIDATE_RANGE_BIT = 0x0004
GL_MAP_INVALIDATE_BUFFER_BIT = 0x0008
GL_MAP_FLUSH_EXPLICIT_BIT = 0x0010
GL_MAP_UNSYNCHRONIZED_BIT = 0x0020
GL_CONTEXT_FLAG_FORWARD_COMPATIBLE_BIT = 0x00000001
GL_CONTEXT_FLAG_DEBUG_BIT = 0x00000002
GL_VERTEX_SHADER_BIT = 0x00000001
GL_FRAGMENT_SHADER_BIT = 0x00000002
GL_GEOMETRY_SHADER_BIT = 0x00000004
GL_TESS_CONTROL_SHADER_BIT = 0x00000008
GL_TESS_EVALUATION_SHADER_BIT = 0x00000010
GL_ALL_SHADER_BITS = 0xFFFFFFFF
GL_COMPUTE_SHADER_BIT = 0x00000020
GL_VERTEX_ATTRIB_ARRAY_BARRIER_BIT = 0x00000001
GL_ELEMENT_ARRAY_BARRIER_BIT = 0x00000002
GL_UNIFORM_BARRIER_BIT = 0x00000004
GL_TEXTURE_FETCH_BARRIER_BIT = 0x00000008
GL_SHADER_IMAGE_ACCESS_BARRIER_BIT = 0x00000020
GL_COMMAND_BARRIER_BIT = 0x00000040
GL_PIXEL_BUFFER_BARRIER_BIT = 0x00000080
GL_TEXTURE_UPDATE_BARRIER_BIT = 0x00000100
GL_BUFFER_UPDATE_BARRIER_BIT = 0x00000200
GL_FRAMEBUFFER_BARRIER_BIT = 0x00000400
GL_TRANSFORM_FEEDBACK_BARRIER_BIT = 0x00000800
GL_ATOMIC_COUNTER_BARRIER_BIT = 0x00001000
GL_ALL_BARRIER_BITS = 0xFFFFFFFF
GL_SHADER_STORAGE_BARRIER_BIT = 0x00002000
GL_FALSE = 0
GL_TRUE = 1
GL_POINTS = 0x0000
GL_LINES = 0x0001
GL_LINE_LOOP = 0x0002
GL_LINE_STRIP = 0x0003
GL_TRIANGLES = 0x0004
GL_TRIANGLE_STRIP = 0x0005
GL_TRIANGLE_FAN = 0x0006
GL_QUADS = 0x0007
GL_QUAD_STRIP = 0x0008
GL_POLYGON = 0x0009
GL_LINES_ADJACENCY = 0x000A
GL_LINE_STRIP_ADJACENCY = 0x000B
GL_TRIANGLES_ADJACENCY = 0x000C
GL_TRIANGLE_STRIP_ADJACENCY = 0x000D
GL_PATCHES = 0x000E
GL_ACCUM = 0x0100
GL_LOAD = 0x0101
GL_RETURN = 0x0102
GL_MULT = 0x0103
GL_ADD = 0x0104
GL_NEVER = 0x0200
GL_LESS = 0x0201
GL_EQUAL = 0x0202
GL_LEQUAL = 0x0203
GL_GREATER = 0x0204
GL_NOTEQUAL = 0x0205
GL_GEQUAL = 0x0206
GL_ALWAYS = 0x0207
GL_ZERO = 0
GL_ONE = 1
GL_SRC_COLOR = 0x0300
GL_ONE_MINUS_SRC_COLOR = 0x0301
GL_SRC_ALPHA = 0x0302
GL_ONE_MINUS_SRC_ALPHA = 0x0303
GL_DST_ALPHA = 0x0304
GL_ONE_MINUS_DST_ALPHA = 0x0305
GL_DST_COLOR = 0x0306
GL_ONE_MINUS_DST_COLOR = 0x0307
GL_SRC_ALPHA_SATURATE = 0x0308
GL_NONE = 0
GL_FRONT_LEFT = 0x0400
GL_FRONT_RIGHT = 0x0401
GL_BACK_LEFT = 0x0402
GL_BACK_RIGHT = 0x0403
GL_FRONT = 0x0404
GL_BACK = 0x0405
GL_LEFT = 0x0406
GL_RIGHT = 0x0407
GL_FRONT_AND_BACK = 0x0408
GL_AUX0 = 0x0409
GL_AUX1 = 0x040A
GL_AUX2 = 0x040B
GL_AUX3 = 0x040C
GL_NO_ERROR = 0
GL_INVALID_ENUM = 0x0500
GL_INVALID_VALUE = 0x0501
GL_INVALID_OPERATION = 0x0502
GL_STACK_OVERFLOW = 0x0503
GL_STACK_UNDERFLOW = 0x0504
GL_OUT_OF_MEMORY = 0x0505
GL_INVALID_FRAMEBUFFER_OPERATION = 0x0506
GL_2D = 0x0600
GL_3D = 0x0601
GL_3D_COLOR = 0x0602
GL_3D_COLOR_TEXTURE = 0x0603
GL_4D_COLOR_TEXTURE = 0x0604
GL_PASS_THROUGH_TOKEN = 0x0700
GL_POINT_TOKEN = 0x0701
GL_LINE_TOKEN = 0x0702
GL_POLYGON_TOKEN = 0x0703
GL_BITMAP_TOKEN = 0x0704
GL_DRAW_PIXEL_TOKEN = 0x0705
GL_COPY_PIXEL_TOKEN = 0x0706
GL_LINE_RESET_TOKEN = 0x0707
GL_EXP = 0x0800
GL_EXP2 = 0x0801
GL_CW = 0x0900
GL_CCW = 0x0901
GL_COEFF = 0x0A00
GL_ORDER = 0x0A01
GL_DOMAIN = 0x0A02
GL_PIXEL_MAP_I_TO_I = 0x0C70
GL_PIXEL_MAP_S_TO_S = 0x0C71
GL_PIXEL_MAP_I_TO_R = 0x0C72
GL_PIXEL_MAP_I_TO_G = 0x0C73
GL_PIXEL_MAP_I_TO_B = 0x0C74
GL_PIXEL_MAP_I_TO_A = 0x0C75
GL_PIXEL_MAP_R_TO_R = 0x0C76
GL_PIXEL_MAP_G_TO_G = 0x0C77
GL_PIXEL_MAP_B_TO_B = 0x0C78
GL_PIXEL_MAP_A_TO_A = 0x0C79
GL_VERTEX_ARRAY_POINTER = 0x808E
GL_NORMAL_ARRAY_POINTER = 0x808F
GL_COLOR_ARRAY_POINTER = 0x8090
GL_INDEX_ARRAY_POINTER = 0x8091
GL_TEXTURE_COORD_ARRAY_POINTER = 0x8092
GL_EDGE_FLAG_ARRAY_POINTER = 0x8093
GL_FEEDBACK_BUFFER_POINTER = 0x0DF0
GL_SELECTION_BUFFER_POINTER = 0x0DF3
GL_CURRENT_COLOR = 0x0B00
GL_CURRENT_INDEX = 0x0B01
GL_CURRENT_NORMAL = 0x0B02
GL_CURRENT_TEXTURE_COORDS = 0x0B03
GL_CURRENT_RASTER_COLOR = 0x0B04
GL_CURRENT_RASTER_INDEX = 0x0B05
GL_CURRENT_RASTER_TEXTURE_COORDS = 0x0B06
GL_CURRENT_RASTER_POSITION = 0x0B07
GL_CURRENT_RASTER_POSITION_VALID = 0x0B08
GL_CURRENT_RASTER_DISTANCE = 0x0B09
GL_POINT_SMOOTH = 0x0B10
GL_POINT_SIZE = 0x0B11
GL_POINT_SIZE_RANGE = 0x0B12
GL_POINT_SIZE_GRANULARITY = 0x0B13
GL_LINE_SMOOTH = 0x0B20
GL_LINE_WIDTH = 0x0B21
GL_LINE_WIDTH_RANGE = 0x0B22
GL_LINE_WIDTH_GRANULARITY = 0x0B23
GL_LINE_STIPPLE = 0x0B24
GL_LINE_STIPPLE_PATTERN = 0x0B25
GL_LINE_STIPPLE_REPEAT = 0x0B26
GL_LIST_MODE = 0x0B30
GL_MAX_LIST_NESTING = 0x0B31
GL_LIST_BASE = 0x0B32
GL_LIST_INDEX = 0x0B33
GL_POLYGON_MODE = 0x0B40
GL_POLYGON_SMOOTH = 0x0B41
GL_POLYGON_STIPPLE = 0x0B42
GL_EDGE_FLAG = 0x0B43
GL_CULL_FACE = 0x0B44
GL_CULL_FACE_MODE = 0x0B45
GL_FRONT_FACE = 0x0B46
GL_LIGHTING = 0x0B50
GL_LIGHT_MODEL_LOCAL_VIEWER = 0x0B51
GL_LIGHT_MODEL_TWO_SIDE = 0x0B52
GL_LIGHT_MODEL_AMBIENT = 0x0B53
GL_SHADE_MODEL = 0x0B54
GL_COLOR_MATERIAL_FACE = 0x0B55
GL_COLOR_MATERIAL_PARAMETER = 0x0B56
GL_COLOR_MATERIAL = 0x0B57
GL_FOG = 0x0B60
GL_FOG_INDEX = 0x0B61
GL_FOG_DENSITY = 0x0B62
GL_FOG_START = 0x0B63
GL_FOG_END = 0x0B64
GL_FOG_MODE = 0x0B65
GL_FOG_COLOR = 0x0B66
GL_DEPTH_RANGE = 0x0B70
GL_DEPTH_TEST = 0x0B71
GL_DEPTH_WRITEMASK = 0x0B72
GL_DEPTH_CLEAR_VALUE = 0x0B73
GL_DEPTH_FUNC = 0x0B74
GL_ACCUM_CLEAR_VALUE = 0x0B80
GL_STENCIL_TEST = 0x0B90
GL_STENCIL_CLEAR_VALUE = 0x0B91
GL_STENCIL_FUNC = 0x0B92
GL_STENCIL_VALUE_MASK = 0x0B93
GL_STENCIL_FAIL = 0x0B94
GL_STENCIL_PASS_DEPTH_FAIL = 0x0B95
GL_STENCIL_PASS_DEPTH_PASS = 0x0B96
GL_STENCIL_REF = 0x0B97
GL_STENCIL_WRITEMASK = 0x0B98
GL_MATRIX_MODE = 0x0BA0
GL_NORMALIZE = 0x0BA1
GL_VIEWPORT = 0x0BA2
GL_MODELVIEW_STACK_DEPTH = 0x0BA3
GL_PROJECTION_STACK_DEPTH = 0x0BA4
GL_TEXTURE_STACK_DEPTH = 0x0BA5
GL_MODELVIEW_MATRIX = 0x0BA6
GL_PROJECTION_MATRIX = 0x0BA7
GL_TEXTURE_MATRIX = 0x0BA8
GL_ATTRIB_STACK_DEPTH = 0x0BB0
GL_CLIENT_ATTRIB_STACK_DEPTH = 0x0BB1
GL_ALPHA_TEST = 0x0BC0
GL_ALPHA_TEST_FUNC = 0x0BC1
GL_ALPHA_TEST_REF = 0x0BC2
GL_DITHER = 0x0BD0
GL_BLEND_DST = 0x0BE0
GL_BLEND_SRC = 0x0BE1
GL_BLEND = 0x0BE2
GL_LOGIC_OP_MODE = 0x0BF0
GL_INDEX_LOGIC_OP = 0x0BF1
GL_LOGIC_OP = 0x0BF1
GL_COLOR_LOGIC_OP = 0x0BF2
GL_AUX_BUFFERS = 0x0C00
GL_DRAW_BUFFER = 0x0C01
GL_READ_BUFFER = 0x0C02
GL_SCISSOR_BOX = 0x0C10
GL_SCISSOR_TEST = 0x0C11
GL_INDEX_CLEAR_VALUE = 0x0C20
GL_INDEX_WRITEMASK = 0x0C21
GL_COLOR_CLEAR_VALUE = 0x0C22
GL_COLOR_WRITEMASK = 0x0C23
GL_INDEX_MODE = 0x0C30
GL_RGBA_MODE = 0x0C31
GL_DOUBLEBUFFER = 0x0C32
GL_STEREO = 0x0C33
GL_RENDER_MODE = 0x0C40
GL_PERSPECTIVE_CORRECTION_HINT = 0x0C50
GL_POINT_SMOOTH_HINT = 0x0C51
GL_LINE_SMOOTH_HINT = 0x0C52
GL_POLYGON_SMOOTH_HINT = 0x0C53
GL_FOG_HINT = 0x0C54
GL_TEXTURE_GEN_S = 0x0C60
GL_TEXTURE_GEN_T = 0x0C61
GL_TEXTURE_GEN_R = 0x0C62
GL_TEXTURE_GEN_Q = 0x0C63
GL_PIXEL_MAP_I_TO_I_SIZE = 0x0CB0
GL_PIXEL_MAP_S_TO_S_SIZE = 0x0CB1
GL_PIXEL_MAP_I_TO_R_SIZE = 0x0CB2
GL_PIXEL_MAP_I_TO_G_SIZE = 0x0CB3
GL_PIXEL_MAP_I_TO_B_SIZE = 0x0CB4
GL_PIXEL_MAP_I_TO_A_SIZE = 0x0CB5
GL_PIXEL_MAP_R_TO_R_SIZE = 0x0CB6
GL_PIXEL_MAP_G_TO_G_SIZE = 0x0CB7
GL_PIXEL_MAP_B_TO_B_SIZE = 0x0CB8
GL_PIXEL_MAP_A_TO_A_SIZE = 0x0CB9
GL_UNPACK_SWAP_BYTES = 0x0CF0
GL_UNPACK_LSB_FIRST = 0x0CF1
GL_UNPACK_ROW_LENGTH = 0x0CF2
GL_UNPACK_SKIP_ROWS = 0x0CF3
GL_UNPACK_SKIP_PIXELS = 0x0CF4
GL_UNPACK_ALIGNMENT = 0x0CF5
GL_PACK_SWAP_BYTES = 0x0D00
GL_PACK_LSB_FIRST = 0x0D01
GL_PACK_ROW_LENGTH = 0x0D02
GL_PACK_SKIP_ROWS = 0x0D03
GL_PACK_SKIP_PIXELS = 0x0D04
GL_PACK_ALIGNMENT = 0x0D05
GL_MAP_COLOR = 0x0D10
GL_MAP_STENCIL = 0x0D11
GL_INDEX_SHIFT = 0x0D12
GL_INDEX_OFFSET = 0x0D13
GL_RED_SCALE = 0x0D14
GL_RED_BIAS = 0x0D15
GL_ZOOM_X = 0x0D16
GL_ZOOM_Y = 0x0D17
GL_GREEN_SCALE = 0x0D18
GL_GREEN_BIAS = 0x0D19
GL_BLUE_SCALE = 0x0D1A
GL_BLUE_BIAS = 0x0D1B
GL_ALPHA_SCALE = 0x0D1C
GL_ALPHA_BIAS = 0x0D1D
GL_DEPTH_SCALE = 0x0D1E
GL_DEPTH_BIAS = 0x0D1F
GL_MAX_EVAL_ORDER = 0x0D30
GL_MAX_LIGHTS = 0x0D31
GL_MAX_CLIP_DISTANCES = 0x0D32
GL_MAX_CLIP_PLANES = 0x0D32
GL_MAX_TEXTURE_SIZE = 0x0D33
GL_MAX_PIXEL_MAP_TABLE = 0x0D34
GL_MAX_ATTRIB_STACK_DEPTH = 0x0D35
GL_MAX_MODELVIEW_STACK_DEPTH = 0x0D36
GL_MAX_NAME_STACK_DEPTH = 0x0D37
GL_MAX_PROJECTION_STACK_DEPTH = 0x0D38
GL_MAX_TEXTURE_STACK_DEPTH = 0x0D39
GL_MAX_VIEWPORT_DIMS = 0x0D3A
GL_MAX_CLIENT_ATTRIB_STACK_DEPTH = 0x0D3B
GL_SUBPIXEL_BITS = 0x0D50
GL_INDEX_BITS = 0x0D51
GL_RED_BITS = 0x0D52
GL_GREEN_BITS = 0x0D53
GL_BLUE_BITS = 0x0D54
GL_ALPHA_BITS = 0x0D55
GL_DEPTH_BITS = 0x0D56
GL_STENCIL_BITS = 0x0D57
GL_ACCUM_RED_BITS = 0x0D58
GL_ACCUM_GREEN_BITS = 0x0D59
GL_ACCUM_BLUE_BITS = 0x0D5A
GL_ACCUM_ALPHA_BITS = 0x0D5B
GL_NAME_STACK_DEPTH = 0x0D70
GL_AUTO_NORMAL = 0x0D80
GL_MAP1_COLOR_4 = 0x0D90
GL_MAP1_INDEX = 0x0D91
GL_MAP1_NORMAL = 0x0D92
GL_MAP1_TEXTURE_COORD_1 = 0x0D93
GL_MAP1_TEXTURE_COORD_2 = 0x0D94
GL_MAP1_TEXTURE_COORD_3 = 0x0D95
GL_MAP1_TEXTURE_COORD_4 = 0x0D96
GL_MAP1_VERTEX_3 = 0x0D97
GL_MAP1_VERTEX_4 = 0x0D98
GL_MAP2_COLOR_4 = 0x0DB0
GL_MAP2_INDEX = 0x0DB1
GL_MAP2_NORMAL = 0x0DB2
GL_MAP2_TEXTURE_COORD_1 = 0x0DB3
GL_MAP2_TEXTURE_COORD_2 = 0x0DB4
GL_MAP2_TEXTURE_COORD_3 = 0x0DB5
GL_MAP2_TEXTURE_COORD_4 = 0x0DB6
GL_MAP2_VERTEX_3 = 0x0DB7
GL_MAP2_VERTEX_4 = 0x0DB8
GL_MAP1_GRID_DOMAIN = 0x0DD0
GL_MAP1_GRID_SEGMENTS = 0x0DD1
GL_MAP2_GRID_DOMAIN = 0x0DD2
GL_MAP2_GRID_SEGMENTS = 0x0DD3
GL_TEXTURE_1D = 0x0DE0
GL_TEXTURE_2D = 0x0DE1
GL_FEEDBACK_BUFFER_SIZE = 0x0DF1
GL_FEEDBACK_BUFFER_TYPE = 0x0DF2
GL_SELECTION_BUFFER_SIZE = 0x0DF4
GL_POLYGON_OFFSET_UNITS = 0x2A00
GL_POLYGON_OFFSET_POINT = 0x2A01
GL_POLYGON_OFFSET_LINE = 0x2A02
GL_POLYGON_OFFSET_FILL = 0x8037
GL_POLYGON_OFFSET_FACTOR = 0x8038
GL_TEXTURE_BINDING_1D = 0x8068
GL_TEXTURE_BINDING_2D = 0x8069
GL_TEXTURE_BINDING_3D = 0x806A
GL_VERTEX_ARRAY = 0x8074
GL_NORMAL_ARRAY = 0x8075
GL_COLOR_ARRAY = 0x8076
GL_INDEX_ARRAY = 0x8077
GL_TEXTURE_COORD_ARRAY = 0x8078
GL_EDGE_FLAG_ARRAY = 0x8079
GL_VERTEX_ARRAY_SIZE = 0x807A
GL_VERTEX_ARRAY_TYPE = 0x807B
GL_VERTEX_ARRAY_STRIDE = 0x807C
GL_NORMAL_ARRAY_TYPE = 0x807E
GL_NORMAL_ARRAY_STRIDE = 0x807F
GL_COLOR_ARRAY_SIZE = 0x8081
GL_COLOR_ARRAY_TYPE = 0x8082
GL_COLOR_ARRAY_STRIDE = 0x8083
GL_INDEX_ARRAY_TYPE = 0x8085
GL_INDEX_ARRAY_STRIDE = 0x8086
GL_TEXTURE_COORD_ARRAY_SIZE = 0x8088
GL_TEXTURE_COORD_ARRAY_TYPE = 0x8089
GL_TEXTURE_COORD_ARRAY_STRIDE = 0x808A
GL_EDGE_FLAG_ARRAY_STRIDE = 0x808C
GL_TEXTURE_WIDTH = 0x1000
GL_TEXTURE_HEIGHT = 0x1001
GL_TEXTURE_INTERNAL_FORMAT = 0x1003
GL_TEXTURE_COMPONENTS = 0x1003
GL_TEXTURE_BORDER_COLOR = 0x1004
GL_TEXTURE_BORDER = 0x1005
GL_TEXTURE_RED_SIZE = 0x805C
GL_TEXTURE_GREEN_SIZE = 0x805D
GL_TEXTURE_BLUE_SIZE = 0x805E
GL_TEXTURE_ALPHA_SIZE = 0x805F
GL_TEXTURE_LUMINANCE_SIZE = 0x8060
GL_TEXTURE_INTENSITY_SIZE = 0x8061
GL_TEXTURE_PRIORITY = 0x8066
GL_TEXTURE_RESIDENT = 0x8067
GL_DONT_CARE = 0x1100
GL_FASTEST = 0x1101
GL_NICEST = 0x1102
GL_AMBIENT = 0x1200
GL_DIFFUSE = 0x1201
GL_SPECULAR = 0x1202
GL_POSITION = 0x1203
GL_SPOT_DIRECTION = 0x1204
GL_SPOT_EXPONENT = 0x1205
GL_SPOT_CUTOFF = 0x1206
GL_CONSTANT_ATTENUATION = 0x1207
GL_LINEAR_ATTENUATION = 0x1208
GL_QUADRATIC_ATTENUATION = 0x1209
GL_COMPILE = 0x1300
GL_COMPILE_AND_EXECUTE = 0x1301
GL_BYTE = 0x1400
GL_UNSIGNED_BYTE = 0x1401
GL_SHORT = 0x1402
GL_UNSIGNED_SHORT = 0x1403
GL_INT = 0x1404
GL_UNSIGNED_INT = 0x1405
GL_FLOAT = 0x1406
GL_2_BYTES = 0x1407
GL_3_BYTES = 0x1408
GL_4_BYTES = 0x1409
GL_DOUBLE = 0x140A
GL_HALF_FLOAT = 0x140B
GL_FIXED = 0x140C
GL_CLEAR = 0x1500
GL_AND = 0x1501
GL_AND_REVERSE = 0x1502
GL_COPY = 0x1503
GL_AND_INVERTED = 0x1504
GL_NOOP = 0x1505
GL_XOR = 0x1506
GL_OR = 0x1507
GL_NOR = 0x1508
GL_EQUIV = 0x1509
GL_INVERT = 0x150A
GL_OR_REVERSE = 0x150B
GL_COPY_INVERTED = 0x150C
GL_OR_INVERTED = 0x150D
GL_NAND = 0x150E
GL_SET = 0x150F
GL_EMISSION = 0x1600
GL_SHININESS = 0x1601
GL_AMBIENT_AND_DIFFUSE = 0x1602
GL_COLOR_INDEXES = 0x1603
GL_MODELVIEW = 0x1700
GL_PROJECTION = 0x1701
GL_TEXTURE = 0x1702
GL_COLOR = 0x1800
GL_DEPTH = 0x1801
GL_STENCIL = 0x1802
GL_COLOR_INDEX = 0x1900
GL_STENCIL_INDEX = 0x1901
GL_DEPTH_COMPONENT = 0x1902
GL_RED = 0x1903
GL_GREEN = 0x1904
GL_BLUE = 0x1905
GL_ALPHA = 0x1906
GL_RGB = 0x1907
GL_RGBA = 0x1908
GL_LUMINANCE = 0x1909
GL_LUMINANCE_ALPHA = 0x190A
GL_BITMAP = 0x1A00
GL_POINT = 0x1B00
GL_LINE = 0x1B01
GL_FILL = 0x1B02
GL_RENDER = 0x1C00
GL_FEEDBACK = 0x1C01
GL_SELECT = 0x1C02
GL_FLAT = 0x1D00
GL_SMOOTH = 0x1D01
GL_KEEP = 0x1E00
GL_REPLACE = 0x1E01
GL_INCR = 0x1E02
GL_DECR = 0x1E03
GL_VENDOR = 0x1F00
GL_RENDERER = 0x1F01
GL_VERSION = 0x1F02
GL_EXTENSIONS = 0x1F03
GL_S = 0x2000
GL_T = 0x2001
GL_R = 0x2002
GL_Q = 0x2003
GL_MODULATE = 0x2100
GL_DECAL = 0x2101
GL_TEXTURE_ENV_MODE = 0x2200
GL_TEXTURE_ENV_COLOR = 0x2201
GL_TEXTURE_ENV = 0x2300
GL_EYE_LINEAR = 0x2400
GL_OBJECT_LINEAR = 0x2401
GL_SPHERE_MAP = 0x2402
GL_TEXTURE_GEN_MODE = 0x2500
GL_OBJECT_PLANE = 0x2501
GL_EYE_PLANE = 0x2502
GL_TEXTURE_GEN_MODE = 0x2500
GL_NEAREST = 0x2600
GL_LINEAR = 0x2601
GL_NEAREST_MIPMAP_NEAREST = 0x2700
GL_LINEAR_MIPMAP_NEAREST = 0x2701
GL_NEAREST_MIPMAP_LINEAR = 0x2702
GL_LINEAR_MIPMAP_LINEAR = 0x2703
GL_TEXTURE_MAG_FILTER = 0x2800
GL_TEXTURE_MIN_FILTER = 0x2801
GL_TEXTURE_WRAP_S = 0x2802
GL_TEXTURE_WRAP_T = 0x2803
GL_PROXY_TEXTURE_1D = 0x8063
GL_PROXY_TEXTURE_2D = 0x8064
GL_CLAMP = 0x2900
GL_REPEAT = 0x2901
GL_R3_G3_B2 = 0x2A10
GL_ALPHA4 = 0x803B
GL_ALPHA8 = 0x803C
GL_ALPHA12 = 0x803D
GL_ALPHA16 = 0x803E
GL_LUMINANCE4 = 0x803F
GL_LUMINANCE8 = 0x8040
GL_LUMINANCE12 = 0x8041
GL_LUMINANCE16 = 0x8042
GL_LUMINANCE4_ALPHA4 = 0x8043
GL_LUMINANCE6_ALPHA2 = 0x8044
GL_LUMINANCE8_ALPHA8 = 0x8045
GL_LUMINANCE12_ALPHA4 = 0x8046
GL_LUMINANCE12_ALPHA12 = 0x8047
GL_LUMINANCE16_ALPHA16 = 0x8048
GL_INTENSITY = 0x8049
GL_INTENSITY4 = 0x804A
GL_INTENSITY8 = 0x804B
GL_INTENSITY12 = 0x804C
GL_INTENSITY16 = 0x804D
GL_RGB4 = 0x804F
GL_RGB5 = 0x8050
GL_RGB8 = 0x8051
GL_RGB10 = 0x8052
GL_RGB12 = 0x8053
GL_RGB16 = 0x8054
GL_RGBA2 = 0x8055
GL_RGBA4 = 0x8056
GL_RGB5_A1 = 0x8057
GL_RGBA8 = 0x8058
GL_RGB10_A2 = 0x8059
GL_RGBA12 = 0x805A
GL_RGBA16 = 0x805B
GL_RGB8 = 0x8051
GL_RGBA8 = 0x8058
GL_V2F = 0x2A20
GL_V3F = 0x2A21
GL_C4UB_V2F = 0x2A22
GL_C4UB_V3F = 0x2A23
GL_C3F_V3F = 0x2A24
GL_N3F_V3F = 0x2A25
GL_C4F_N3F_V3F = 0x2A26
GL_T2F_V3F = 0x2A27
GL_T4F_V4F = 0x2A28
GL_T2F_C4UB_V3F = 0x2A29
GL_T2F_C3F_V3F = 0x2A2A
GL_T2F_N3F_V3F = 0x2A2B
GL_T2F_C4F_N3F_V3F = 0x2A2C
GL_T4F_C4F_N3F_V4F = 0x2A2D
GL_CLIP_PLANE0 = 0x3000
GL_CLIP_PLANE1 = 0x3001
GL_CLIP_PLANE2 = 0x3002
GL_CLIP_PLANE3 = 0x3003
GL_CLIP_PLANE4 = 0x3004
GL_CLIP_PLANE5 = 0x3005
GL_CLIP_DISTANCE0 = 0x3000
GL_CLIP_DISTANCE1 = 0x3001
GL_CLIP_DISTANCE2 = 0x3002
GL_CLIP_DISTANCE3 = 0x3003
GL_CLIP_DISTANCE4 = 0x3004
GL_CLIP_DISTANCE5 = 0x3005
GL_CLIP_DISTANCE6 = 0x3006
GL_CLIP_DISTANCE7 = 0x3007
GL_LIGHT0 = 0x4000
GL_LIGHT1 = 0x4001
GL_LIGHT2 = 0x4002
GL_LIGHT3 = 0x4003
GL_LIGHT4 = 0x4004
GL_LIGHT5 = 0x4005
GL_LIGHT6 = 0x4006
GL_LIGHT7 = 0x4007
GL_CONSTANT_COLOR = 0x8001
GL_ONE_MINUS_CONSTANT_COLOR = 0x8002
GL_CONSTANT_ALPHA = 0x8003
GL_ONE_MINUS_CONSTANT_ALPHA = 0x8004
GL_BLEND_COLOR = 0x8005
GL_FUNC_ADD = 0x8006
GL_MIN = 0x8007
GL_MAX = 0x8008
GL_BLEND_EQUATION = 0x8009
GL_BLEND_EQUATION_RGB = 0x8009
GL_FUNC_SUBTRACT = 0x800A
GL_FUNC_REVERSE_SUBTRACT = 0x800B
GL_CONVOLUTION_1D = 0x8010
GL_CONVOLUTION_2D = 0x8011
GL_SEPARABLE_2D = 0x8012
GL_CONVOLUTION_BORDER_MODE = 0x8013
GL_CONVOLUTION_FILTER_SCALE = 0x8014
GL_CONVOLUTION_FILTER_BIAS = 0x8015
GL_REDUCE = 0x8016
GL_CONVOLUTION_FORMAT = 0x8017
GL_CONVOLUTION_WIDTH = 0x8018
GL_CONVOLUTION_HEIGHT = 0x8019
GL_MAX_CONVOLUTION_WIDTH = 0x801A
GL_MAX_CONVOLUTION_HEIGHT = 0x801B
GL_POST_CONVOLUTION_RED_SCALE = 0x801C
GL_POST_CONVOLUTION_GREEN_SCALE = 0x801D
GL_POST_CONVOLUTION_BLUE_SCALE = 0x801E
GL_POST_CONVOLUTION_ALPHA_SCALE = 0x801F
GL_POST_CONVOLUTION_RED_BIAS = 0x8020
GL_POST_CONVOLUTION_GREEN_BIAS = 0x8021
GL_POST_CONVOLUTION_BLUE_BIAS = 0x8022
GL_POST_CONVOLUTION_ALPHA_BIAS = 0x8023
GL_HISTOGRAM = 0x8024
GL_PROXY_HISTOGRAM = 0x8025
GL_HISTOGRAM_WIDTH = 0x8026
GL_HISTOGRAM_FORMAT = 0x8027
GL_HISTOGRAM_RED_SIZE = 0x8028
GL_HISTOGRAM_GREEN_SIZE = 0x8029
GL_HISTOGRAM_BLUE_SIZE = 0x802A
GL_HISTOGRAM_ALPHA_SIZE = 0x802B
GL_HISTOGRAM_SINK = 0x802D
GL_MINMAX = 0x802E
GL_MINMAX_FORMAT = 0x802F
GL_MINMAX_SINK = 0x8030
GL_TABLE_TOO_LARGE = 0x8031
GL_HISTOGRAM_LUMINANCE_SIZE = 0x802C
GL_UNSIGNED_BYTE_3_3_2 = 0x8032
GL_UNSIGNED_SHORT_4_4_4_4 = 0x8033
GL_UNSIGNED_SHORT_5_5_5_1 = 0x8034
GL_UNSIGNED_INT_8_8_8_8 = 0x8035
GL_UNSIGNED_INT_10_10_10_2 = 0x8036
GL_UNSIGNED_BYTE_2_3_3_REV = 0x8362
GL_UNSIGNED_SHORT_5_6_5 = 0x8363
GL_UNSIGNED_SHORT_5_6_5_REV = 0x8364
GL_UNSIGNED_SHORT_4_4_4_4_REV = 0x8365
GL_UNSIGNED_SHORT_1_5_5_5_REV = 0x8366
GL_UNSIGNED_INT_8_8_8_8_REV = 0x8367
GL_UNSIGNED_INT_2_10_10_10_REV = 0x8368
GL_RESCALE_NORMAL = 0x803A
GL_PACK_SKIP_IMAGES = 0x806B
GL_PACK_IMAGE_HEIGHT = 0x806C
GL_UNPACK_SKIP_IMAGES = 0x806D
GL_UNPACK_IMAGE_HEIGHT = 0x806E
GL_TEXTURE_3D = 0x806F
GL_PROXY_TEXTURE_3D = 0x8070
GL_TEXTURE_DEPTH = 0x8071
GL_TEXTURE_WRAP_R = 0x8072
GL_MAX_3D_TEXTURE_SIZE = 0x8073
GL_MULTISAMPLE = 0x809D
GL_SAMPLE_ALPHA_TO_COVERAGE = 0x809E
GL_SAMPLE_ALPHA_TO_ONE = 0x809F
GL_SAMPLE_COVERAGE = 0x80A0
GL_SAMPLE_BUFFERS = 0x80A8
GL_SAMPLES = 0x80A9
GL_SAMPLE_COVERAGE_VALUE = 0x80AA
GL_SAMPLE_COVERAGE_INVERT = 0x80AB
GL_COLOR_MATRIX = 0x80B1
GL_COLOR_MATRIX_STACK_DEPTH = 0x80B2
GL_MAX_COLOR_MATRIX_STACK_DEPTH = 0x80B3
GL_POST_COLOR_MATRIX_RED_SCALE = 0x80B4
GL_POST_COLOR_MATRIX_GREEN_SCALE = 0x80B5
GL_POST_COLOR_MATRIX_BLUE_SCALE = 0x80B6
GL_POST_COLOR_MATRIX_ALPHA_SCALE = 0x80B7
GL_POST_COLOR_MATRIX_RED_BIAS = 0x80B8
GL_POST_COLOR_MATRIX_GREEN_BIAS = 0x80B9
GL_POST_COLOR_MATRIX_BLUE_BIAS = 0x80BA
GL_POST_COLOR_MATRIX_ALPHA_BIAS = 0x80BB
GL_BLEND_DST_RGB = 0x80C8
GL_BLEND_SRC_RGB = 0x80C9
GL_BLEND_DST_ALPHA = 0x80CA
GL_BLEND_SRC_ALPHA = 0x80CB
GL_COLOR_TABLE = 0x80D0
GL_POST_CONVOLUTION_COLOR_TABLE = 0x80D1
GL_POST_COLOR_MATRIX_COLOR_TABLE = 0x80D2
GL_PROXY_COLOR_TABLE = 0x80D3
GL_PROXY_POST_CONVOLUTION_COLOR_TABLE = 0x80D4
GL_PROXY_POST_COLOR_MATRIX_COLOR_TABLE = 0x80D5
GL_COLOR_TABLE_SCALE = 0x80D6
GL_COLOR_TABLE_BIAS = 0x80D7
GL_COLOR_TABLE_FORMAT = 0x80D8
GL_COLOR_TABLE_WIDTH = 0x80D9
GL_COLOR_TABLE_RED_SIZE = 0x80DA
GL_COLOR_TABLE_GREEN_SIZE = 0x80DB
GL_COLOR_TABLE_BLUE_SIZE = 0x80DC
GL_COLOR_TABLE_ALPHA_SIZE = 0x80DD
GL_COLOR_TABLE_LUMINANCE_SIZE = 0x80DE
GL_COLOR_TABLE_INTENSITY_SIZE = 0x80DF
GL_BGR = 0x80E0
GL_BGRA = 0x80E1
GL_MAX_ELEMENTS_VERTICES = 0x80E8
GL_MAX_ELEMENTS_INDICES = 0x80E9
GL_POINT_SIZE_MIN = 0x8126
GL_POINT_SIZE_MAX = 0x8127
GL_POINT_FADE_THRESHOLD_SIZE = 0x8128
GL_POINT_DISTANCE_ATTENUATION = 0x8129
GL_CLAMP_TO_BORDER = 0x812D
GL_CLAMP_TO_EDGE = 0x812F
GL_TEXTURE_MIN_LOD = 0x813A
GL_TEXTURE_MAX_LOD = 0x813B
GL_TEXTURE_BASE_LEVEL = 0x813C
GL_TEXTURE_MAX_LEVEL = 0x813D
GL_CONSTANT_BORDER = 0x8151
GL_REPLICATE_BORDER = 0x8153
GL_CONVOLUTION_BORDER_COLOR = 0x8154
GL_GENERATE_MIPMAP = 0x8191
GL_GENERATE_MIPMAP_HINT = 0x8192
GL_DEPTH_COMPONENT16 = 0x81A5
GL_DEPTH_COMPONENT24 = 0x81A6
GL_DEPTH_COMPONENT32 = 0x81A7
GL_LIGHT_MODEL_COLOR_CONTROL = 0x81F8
GL_SINGLE_COLOR = 0x81F9
GL_SEPARATE_SPECULAR_COLOR = 0x81FA
GL_FRAMEBUFFER_ATTACHMENT_COLOR_ENCODING = 0x8210
GL_FRAMEBUFFER_ATTACHMENT_COMPONENT_TYPE = 0x8211
GL_FRAMEBUFFER_ATTACHMENT_RED_SIZE = 0x8212
GL_FRAMEBUFFER_ATTACHMENT_GREEN_SIZE = 0x8213
GL_FRAMEBUFFER_ATTACHMENT_BLUE_SIZE = 0x8214
GL_FRAMEBUFFER_ATTACHMENT_ALPHA_SIZE = 0x8215
GL_FRAMEBUFFER_ATTACHMENT_DEPTH_SIZE = 0x8216
GL_FRAMEBUFFER_ATTACHMENT_STENCIL_SIZE = 0x8217
GL_FRAMEBUFFER_DEFAULT = 0x8218
GL_FRAMEBUFFER_UNDEFINED = 0x8219
GL_DEPTH_STENCIL_ATTACHMENT = 0x821A
GL_MAJOR_VERSION = 0x821B
GL_MINOR_VERSION = 0x821C
GL_NUM_EXTENSIONS = 0x821D
GL_CONTEXT_FLAGS = 0x821E
GL_INDEX = 0x8222
GL_COMPRESSED_RED = 0x8225
GL_COMPRESSED_RG = 0x8226
GL_RG = 0x8227
GL_RG_INTEGER = 0x8228
GL_R8 = 0x8229
GL_R16 = 0x822A
GL_RG8 = 0x822B
GL_RG16 = 0x822C
GL_R16F = 0x822D
GL_R32F = 0x822E
GL_RG16F = 0x822F
GL_RG32F = 0x8230
GL_R8I = 0x8231
GL_R8UI = 0x8232
GL_R16I = 0x8233
GL_R16UI = 0x8234
GL_R32I = 0x8235
GL_R32UI = 0x8236
GL_RG8I = 0x8237
GL_RG8UI = 0x8238
GL_RG16I = 0x8239
GL_RG16UI = 0x823A
GL_RG32I = 0x823B
GL_RG32UI = 0x823C
GL_DEBUG_OUTPUT_SYNCHRONOUS = 0x8242
GL_DEBUG_NEXT_LOGGED_MESSAGE_LENGTH = 0x8243
GL_DEBUG_CALLBACK_FUNCTION = 0x8244
GL_DEBUG_CALLBACK_USER_PARAM = 0x8245
GL_DEBUG_SOURCE_API = 0x8246
GL_DEBUG_SOURCE_WINDOW_SYSTEM = 0x8247
GL_DEBUG_SOURCE_SHADER_COMPILER = 0x8248
GL_DEBUG_SOURCE_THIRD_PARTY = 0x8249
GL_DEBUG_SOURCE_APPLICATION = 0x824A
GL_DEBUG_SOURCE_OTHER = 0x824B
GL_DEBUG_TYPE_ERROR = 0x824C
GL_DEBUG_TYPE_DEPRECATED_BEHAVIOR = 0x824D
GL_DEBUG_TYPE_UNDEFINED_BEHAVIOR = 0x824E
GL_DEBUG_TYPE_PORTABILITY = 0x824F
GL_DEBUG_TYPE_PERFORMANCE = 0x8250
GL_DEBUG_TYPE_OTHER = 0x8251
GL_PROGRAM_BINARY_RETRIEVABLE_HINT = 0x8257
GL_PROGRAM_SEPARABLE = 0x8258
GL_ACTIVE_PROGRAM = 0x8259
GL_PROGRAM_PIPELINE_BINDING = 0x825A
GL_MAX_VIEWPORTS = 0x825B
GL_VIEWPORT_SUBPIXEL_BITS = 0x825C
GL_VIEWPORT_BOUNDS_RANGE = 0x825D
GL_LAYER_PROVOKING_VERTEX = 0x825E
GL_VIEWPORT_INDEX_PROVOKING_VERTEX = 0x825F
GL_UNDEFINED_VERTEX = 0x8260
GL_MAX_COMPUTE_SHARED_MEMORY_SIZE = 0x8262
GL_MAX_COMPUTE_UNIFORM_COMPONENTS = 0x8263
GL_MAX_COMPUTE_ATOMIC_COUNTER_BUFFERS = 0x8264
GL_MAX_COMPUTE_ATOMIC_COUNTERS = 0x8265
GL_MAX_COMBINED_COMPUTE_UNIFORM_COMPONENTS = 0x8266
GL_COMPUTE_LOCAL_WORK_SIZE = 0x8267
GL_DEBUG_TYPE_MARKER = 0x8268
GL_DEBUG_TYPE_PUSH_GROUP = 0x8269
GL_DEBUG_TYPE_POP_GROUP = 0x826A
GL_DEBUG_SEVERITY_NOTIFICATION = 0x826B
GL_MAX_DEBUG_GROUP_STACK_DEPTH = 0x826C
GL_DEBUG_GROUP_STACK_DEPTH = 0x826D
GL_MAX_UNIFORM_LOCATIONS = 0x826E
GL_INTERNALFORMAT_SUPPORTED = 0x826F
GL_INTERNALFORMAT_PREFERRED = 0x8270
GL_INTERNALFORMAT_RED_SIZE = 0x8271
GL_INTERNALFORMAT_GREEN_SIZE = 0x8272
GL_INTERNALFORMAT_BLUE_SIZE = 0x8273
GL_INTERNALFORMAT_ALPHA_SIZE = 0x8274
GL_INTERNALFORMAT_DEPTH_SIZE = 0x8275
GL_INTERNALFORMAT_STENCIL_SIZE = 0x8276
GL_INTERNALFORMAT_SHARED_SIZE = 0x8277
GL_INTERNALFORMAT_RED_TYPE = 0x8278
GL_INTERNALFORMAT_GREEN_TYPE = 0x8279
GL_INTERNALFORMAT_BLUE_TYPE = 0x827A
GL_INTERNALFORMAT_ALPHA_TYPE = 0x827B
GL_INTERNALFORMAT_DEPTH_TYPE = 0x827C
GL_INTERNALFORMAT_STENCIL_TYPE = 0x827D
GL_MAX_WIDTH = 0x827E
GL_MAX_HEIGHT = 0x827F
GL_MAX_DEPTH = 0x8280
GL_MAX_LAYERS = 0x8281
GL_MAX_COMBINED_DIMENSIONS = 0x8282
GL_COLOR_COMPONENTS = 0x8283
GL_DEPTH_COMPONENTS = 0x8284
GL_STENCIL_COMPONENTS = 0x8285
GL_COLOR_RENDERABLE = 0x8286
GL_DEPTH_RENDERABLE = 0x8287
GL_STENCIL_RENDERABLE = 0x8288
GL_FRAMEBUFFER_RENDERABLE = 0x8289
GL_FRAMEBUFFER_RENDERABLE_LAYERED = 0x828A
GL_FRAMEBUFFER_BLEND = 0x828B
GL_READ_PIXELS = 0x828C
GL_READ_PIXELS_FORMAT = 0x828D
GL_READ_PIXELS_TYPE = 0x828E
GL_TEXTURE_IMAGE_FORMAT = 0x828F
GL_TEXTURE_IMAGE_TYPE = 0x8290
GL_GET_TEXTURE_IMAGE_FORMAT = 0x8291
GL_GET_TEXTURE_IMAGE_TYPE = 0x8292
GL_MIPMAP = 0x8293
GL_MANUAL_GENERATE_MIPMAP = 0x8294
GL_AUTO_GENERATE_MIPMAP = 0x8295
GL_COLOR_ENCODING = 0x8296
GL_SRGB_READ = 0x8297
GL_SRGB_WRITE = 0x8298
GL_FILTER = 0x829A
GL_VERTEX_TEXTURE = 0x829B
GL_TESS_CONTROL_TEXTURE = 0x829C
GL_TESS_EVALUATION_TEXTURE = 0x829D
GL_GEOMETRY_TEXTURE = 0x829E
GL_FRAGMENT_TEXTURE = 0x829F
GL_COMPUTE_TEXTURE = 0x82A0
GL_TEXTURE_SHADOW = 0x82A1
GL_TEXTURE_GATHER = 0x82A2
GL_TEXTURE_GATHER_SHADOW = 0x82A3
GL_SHADER_IMAGE_LOAD = 0x82A4
GL_SHADER_IMAGE_STORE = 0x82A5
GL_SHADER_IMAGE_ATOMIC = 0x82A6
GL_IMAGE_TEXEL_SIZE = 0x82A7
GL_IMAGE_COMPATIBILITY_CLASS = 0x82A8
GL_IMAGE_PIXEL_FORMAT = 0x82A9
GL_IMAGE_PIXEL_TYPE = 0x82AA
GL_SIMULTANEOUS_TEXTURE_AND_DEPTH_TEST = 0x82AC
GL_SIMULTANEOUS_TEXTURE_AND_STENCIL_TEST = 0x82AD
GL_SIMULTANEOUS_TEXTURE_AND_DEPTH_WRITE = 0x82AE
GL_SIMULTANEOUS_TEXTURE_AND_STENCIL_WRITE = 0x82AF
GL_TEXTURE_COMPRESSED_BLOCK_WIDTH = 0x82B1
GL_TEXTURE_COMPRESSED_BLOCK_HEIGHT = 0x82B2
GL_TEXTURE_COMPRESSED_BLOCK_SIZE = 0x82B3
GL_CLEAR_BUFFER = 0x82B4
GL_TEXTURE_VIEW = 0x82B5
GL_VIEW_COMPATIBILITY_CLASS = 0x82B6
GL_FULL_SUPPORT = 0x82B7
GL_CAVEAT_SUPPORT = 0x82B8
GL_IMAGE_CLASS_4_X_32 = 0x82B9
GL_IMAGE_CLASS_2_X_32 = 0x82BA
GL_IMAGE_CLASS_1_X_32 = 0x82BB
GL_IMAGE_CLASS_4_X_16 = 0x82BC
GL_IMAGE_CLASS_2_X_16 = 0x82BD
GL_IMAGE_CLASS_1_X_16 = 0x82BE
GL_IMAGE_CLASS_4_X_8 = 0x82BF
GL_IMAGE_CLASS_2_X_8 = 0x82C0
GL_IMAGE_CLASS_1_X_8 = 0x82C1
GL_IMAGE_CLASS_11_11_10 = 0x82C2
GL_IMAGE_CLASS_10_10_10_2 = 0x82C3
GL_VIEW_CLASS_128_BITS = 0x82C4
GL_VIEW_CLASS_96_BITS = 0x82C5
GL_VIEW_CLASS_64_BITS = 0x82C6
GL_VIEW_CLASS_48_BITS = 0x82C7
GL_VIEW_CLASS_32_BITS = 0x82C8
GL_VIEW_CLASS_24_BITS = 0x82C9
GL_VIEW_CLASS_16_BITS = 0x82CA
GL_VIEW_CLASS_8_BITS = 0x82CB
GL_VIEW_CLASS_S3TC_DXT1_RGB = 0x82CC
GL_VIEW_CLASS_S3TC_DXT1_RGBA = 0x82CD
GL_VIEW_CLASS_S3TC_DXT3_RGBA = 0x82CE
GL_VIEW_CLASS_S3TC_DXT5_RGBA = 0x82CF
GL_VIEW_CLASS_RGTC1_RED = 0x82D0
GL_VIEW_CLASS_RGTC2_RG = 0x82D1
GL_VIEW_CLASS_BPTC_UNORM = 0x82D2
GL_VIEW_CLASS_BPTC_FLOAT = 0x82D3
GL_VERTEX_ATTRIB_BINDING = 0x82D4
GL_VERTEX_ATTRIB_RELATIVE_OFFSET = 0x82D5
GL_VERTEX_BINDING_DIVISOR = 0x82D6
GL_VERTEX_BINDING_OFFSET = 0x82D7
GL_VERTEX_BINDING_STRIDE = 0x82D8
GL_MAX_VERTEX_ATTRIB_RELATIVE_OFFSET = 0x82D9
GL_MAX_VERTEX_ATTRIB_BINDINGS = 0x82DA
GL_TEXTURE_VIEW_MIN_LEVEL = 0x82DB
GL_TEXTURE_VIEW_NUM_LEVELS = 0x82DC
GL_TEXTURE_VIEW_MIN_LAYER = 0x82DD
GL_TEXTURE_VIEW_NUM_LAYERS = 0x82DE
GL_TEXTURE_IMMUTABLE_LEVELS = 0x82DF
GL_BUFFER = 0x82E0
GL_SHADER = 0x82E1
GL_PROGRAM = 0x82E2
GL_QUERY = 0x82E3
GL_PROGRAM_PIPELINE = 0x82E4
GL_SAMPLER = 0x82E6
GL_DISPLAY_LIST = 0x82E7
GL_MAX_LABEL_LENGTH = 0x82E8
GL_NUM_SHADING_LANGUAGE_VERSIONS = 0x82E9
GL_MIRRORED_REPEAT = 0x8370
GL_RGB_S3TC = 0x83A0
GL_RGB4_S3TC = 0x83A1
GL_RGBA_S3TC = 0x83A2
GL_RGBA4_S3TC = 0x83A3
GL_RGBA_DXT5_S3TC = 0x83A4
GL_RGBA4_DXT5_S3TC = 0x83A5
GL_COMPRESSED_RGBA_S3TC_DXT3_ANGLE = 0x83F2
GL_COMPRESSED_RGBA_S3TC_DXT5_ANGLE = 0x83F3
GL_FOG_COORD_SRC = 0x8450
GL_FOG_COORD = 0x8451
GL_CURRENT_FOG_COORD = 0x8453
GL_FOG_COORD_ARRAY_TYPE = 0x8454
GL_FOG_COORD_ARRAY_STRIDE = 0x8455
GL_FOG_COORD_ARRAY_POINTER = 0x8456
GL_FOG_COORD_ARRAY = 0x8457
GL_FOG_COORDINATE_SOURCE = 0x8450
GL_FOG_COORDINATE = 0x8451
GL_FRAGMENT_DEPTH = 0x8452
GL_CURRENT_FOG_COORDINATE = 0x8453
GL_FOG_COORDINATE_ARRAY_TYPE = 0x8454
GL_FOG_COORDINATE_ARRAY_STRIDE = 0x8455
GL_FOG_COORDINATE_ARRAY_POINTER = 0x8456
GL_FOG_COORDINATE_ARRAY = 0x8457
GL_COLOR_SUM = 0x8458
GL_CURRENT_SECONDARY_COLOR = 0x8459
GL_SECONDARY_COLOR_ARRAY_SIZE = 0x845A
GL_SECONDARY_COLOR_ARRAY_TYPE = 0x845B
GL_SECONDARY_COLOR_ARRAY_STRIDE = 0x845C
GL_SECONDARY_COLOR_ARRAY_POINTER = 0x845D
GL_SECONDARY_COLOR_ARRAY = 0x845E
GL_CURRENT_RASTER_SECONDARY_COLOR = 0x845F
GL_SMOOTH_POINT_SIZE_RANGE = 0x0B12
GL_SMOOTH_POINT_SIZE_GRANULARITY = 0x0B13
GL_SMOOTH_LINE_WIDTH_RANGE = 0x0B22
GL_SMOOTH_LINE_WIDTH_GRANULARITY = 0x0B23
GL_ALIASED_POINT_SIZE_RANGE = 0x846D
GL_ALIASED_LINE_WIDTH_RANGE = 0x846E
GL_SCREEN_COORDINATES_REND = 0x8490
GL_INVERTED_SCREEN_W_REND = 0x8491
GL_TEXTURE0 = 0x84C0
GL_TEXTURE1 = 0x84C1
GL_TEXTURE2 = 0x84C2
GL_TEXTURE3 = 0x84C3
GL_TEXTURE4 = 0x84C4
GL_TEXTURE5 = 0x84C5
GL_TEXTURE6 = 0x84C6
GL_TEXTURE7 = 0x84C7
GL_TEXTURE8 = 0x84C8
GL_TEXTURE9 = 0x84C9
GL_TEXTURE10 = 0x84CA
GL_TEXTURE11 = 0x84CB
GL_TEXTURE12 = 0x84CC
GL_TEXTURE13 = 0x84CD
GL_TEXTURE14 = 0x84CE
GL_TEXTURE15 = 0x84CF
GL_TEXTURE16 = 0x84D0
GL_TEXTURE17 = 0x84D1
GL_TEXTURE18 = 0x84D2
GL_TEXTURE19 = 0x84D3
GL_TEXTURE20 = 0x84D4
GL_TEXTURE21 = 0x84D5
GL_TEXTURE22 = 0x84D6
GL_TEXTURE23 = 0x84D7
GL_TEXTURE24 = 0x84D8
GL_TEXTURE25 = 0x84D9
GL_TEXTURE26 = 0x84DA
GL_TEXTURE27 = 0x84DB
GL_TEXTURE28 = 0x84DC
GL_TEXTURE29 = 0x84DD
GL_TEXTURE30 = 0x84DE
GL_TEXTURE31 = 0x84DF
GL_ACTIVE_TEXTURE = 0x84E0
GL_CLIENT_ACTIVE_TEXTURE = 0x84E1
GL_MAX_TEXTURE_UNITS = 0x84E2
GL_TRANSPOSE_MODELVIEW_MATRIX = 0x84E3
GL_TRANSPOSE_PROJECTION_MATRIX = 0x84E4
GL_TRANSPOSE_TEXTURE_MATRIX = 0x84E5
GL_TRANSPOSE_COLOR_MATRIX = 0x84E6
GL_SUBTRACT = 0x84E7
GL_MAX_RENDERBUFFER_SIZE = 0x84E8
GL_COMPRESSED_ALPHA = 0x84E9
GL_COMPRESSED_LUMINANCE = 0x84EA
GL_COMPRESSED_LUMINANCE_ALPHA = 0x84EB
GL_COMPRESSED_INTENSITY = 0x84EC
GL_COMPRESSED_RGB = 0x84ED
GL_COMPRESSED_RGBA = 0x84EE
GL_TEXTURE_COMPRESSION_HINT = 0x84EF
GL_TEXTURE_COMPRESSED_IMAGE_SIZE = 0x86A0
GL_TEXTURE_COMPRESSED = 0x86A1
GL_NUM_COMPRESSED_TEXTURE_FORMATS = 0x86A2
GL_COMPRESSED_TEXTURE_FORMATS = 0x86A3
GL_UNIFORM_BLOCK_REFERENCED_BY_TESS_CONTROL_SHADER = 0x84F0
GL_UNIFORM_BLOCK_REFERENCED_BY_TESS_EVALUATION_SHADER = 0x84F1
GL_TEXTURE_RECTANGLE = 0x84F5
GL_TEXTURE_BINDING_RECTANGLE = 0x84F6
GL_PROXY_TEXTURE_RECTANGLE = 0x84F7
GL_MAX_RECTANGLE_TEXTURE_SIZE = 0x84F8
GL_DEPTH_STENCIL = 0x84F9
GL_UNSIGNED_INT_24_8 = 0x84FA
GL_MAX_TEXTURE_LOD_BIAS = 0x84FD
GL_TEXTURE_FILTER_CONTROL = 0x8500
GL_TEXTURE_LOD_BIAS = 0x8501
GL_INCR_WRAP = 0x8507
GL_DECR_WRAP = 0x8508
GL_NORMAL_MAP = 0x8511
GL_REFLECTION_MAP = 0x8512
GL_TEXTURE_CUBE_MAP = 0x8513
GL_TEXTURE_BINDING_CUBE_MAP = 0x8514
GL_TEXTURE_CUBE_MAP_POSITIVE_X = 0x8515
GL_TEXTURE_CUBE_MAP_NEGATIVE_X = 0x8516
GL_TEXTURE_CUBE_MAP_POSITIVE_Y = 0x8517
GL_TEXTURE_CUBE_MAP_NEGATIVE_Y = 0x8518
GL_TEXTURE_CUBE_MAP_POSITIVE_Z = 0x8519
GL_TEXTURE_CUBE_MAP_NEGATIVE_Z = 0x851A
GL_PROXY_TEXTURE_CUBE_MAP = 0x851B
GL_MAX_CUBE_MAP_TEXTURE_SIZE = 0x851C
GL_NORMAL_MAP = 0x8511
GL_REFLECTION_MAP = 0x8512
GL_RED_MIN_CLAMP_INGR = 0x8560
GL_GREEN_MIN_CLAMP_INGR = 0x8561
GL_BLUE_MIN_CLAMP_INGR = 0x8562
GL_ALPHA_MIN_CLAMP_INGR = 0x8563
GL_RED_MAX_CLAMP_INGR = 0x8564
GL_GREEN_MAX_CLAMP_INGR = 0x8565
GL_BLUE_MAX_CLAMP_INGR = 0x8566
GL_ALPHA_MAX_CLAMP_INGR = 0x8567
GL_INTERLACE_READ_INGR = 0x8568
GL_SRC0_RGB = 0x8580
GL_SRC1_RGB = 0x8581
GL_SRC2_RGB = 0x8582
GL_SRC0_ALPHA = 0x8588
GL_SRC1_ALPHA = 0x8589
GL_SRC2_ALPHA = 0x858A
GL_COMBINE = 0x8570
GL_COMBINE_RGB = 0x8571
GL_COMBINE_ALPHA = 0x8572
GL_RGB_SCALE = 0x8573
GL_ADD_SIGNED = 0x8574
GL_INTERPOLATE = 0x8575
GL_CONSTANT = 0x8576
GL_PRIMARY_COLOR = 0x8577
GL_PREVIOUS = 0x8578
GL_SOURCE0_RGB = 0x8580
GL_SOURCE1_RGB = 0x8581
GL_SOURCE2_RGB = 0x8582
GL_SOURCE0_ALPHA = 0x8588
GL_SOURCE1_ALPHA = 0x8589
GL_SOURCE2_ALPHA = 0x858A
GL_OPERAND0_RGB = 0x8590
GL_OPERAND1_RGB = 0x8591
GL_OPERAND2_RGB = 0x8592
GL_OPERAND0_ALPHA = 0x8598
GL_OPERAND1_ALPHA = 0x8599
GL_OPERAND2_ALPHA = 0x859A
GL_VERTEX_ARRAY_BINDING = 0x85B5
GL_PROGRAM_POINT_SIZE = 0x8642
GL_DEPTH_CLAMP = 0x864F
GL_VERTEX_ATTRIB_ARRAY_ENABLED = 0x8622
GL_VERTEX_ATTRIB_ARRAY_SIZE = 0x8623
GL_VERTEX_ATTRIB_ARRAY_STRIDE = 0x8624
GL_VERTEX_ATTRIB_ARRAY_TYPE = 0x8625
GL_CURRENT_VERTEX_ATTRIB = 0x8626
GL_VERTEX_PROGRAM_POINT_SIZE = 0x8642
GL_VERTEX_PROGRAM_TWO_SIDE = 0x8643
GL_VERTEX_ATTRIB_ARRAY_POINTER = 0x8645
GL_DOT3_RGB = 0x86AE
GL_DOT3_RGBA = 0x86AF
GL_DOT3_RGBA_IMG = 0x86AF
GL_PROGRAM_BINARY_LENGTH = 0x8741
GL_VERTEX_ATTRIB_ARRAY_LONG = 0x874E
GL_BUFFER_SIZE = 0x8764
GL_BUFFER_USAGE = 0x8765
GL_NUM_PROGRAM_BINARY_FORMATS = 0x87FE
GL_PROGRAM_BINARY_FORMATS = 0x87FF
GL_STENCIL_BACK_FUNC = 0x8800
GL_STENCIL_BACK_FAIL = 0x8801
GL_STENCIL_BACK_PASS_DEPTH_FAIL = 0x8802
GL_STENCIL_BACK_PASS_DEPTH_PASS = 0x8803
GL_RGBA32F = 0x8814
GL_RGB32F = 0x8815
GL_RGBA16F = 0x881A
GL_RGB16F = 0x881B
GL_MAX_DRAW_BUFFERS = 0x8824
GL_DRAW_BUFFER0 = 0x8825
GL_DRAW_BUFFER1 = 0x8826
GL_DRAW_BUFFER2 = 0x8827
GL_DRAW_BUFFER3 = 0x8828
GL_DRAW_BUFFER4 = 0x8829
GL_DRAW_BUFFER5 = 0x882A
GL_DRAW_BUFFER6 = 0x882B
GL_DRAW_BUFFER7 = 0x882C
GL_DRAW_BUFFER8 = 0x882D
GL_DRAW_BUFFER9 = 0x882E
GL_DRAW_BUFFER10 = 0x882F
GL_DRAW_BUFFER11 = 0x8830
GL_DRAW_BUFFER12 = 0x8831
GL_DRAW_BUFFER13 = 0x8832
GL_DRAW_BUFFER14 = 0x8833
GL_DRAW_BUFFER15 = 0x8834
GL_BLEND_EQUATION_ALPHA = 0x883D
GL_TEXTURE_DEPTH_SIZE = 0x884A
GL_DEPTH_TEXTURE_MODE = 0x884B
GL_COMPARE_REF_TO_TEXTURE = 0x884E
GL_TEXTURE_COMPARE_MODE = 0x884C
GL_TEXTURE_COMPARE_FUNC = 0x884D
GL_COMPARE_R_TO_TEXTURE = 0x884E
GL_TEXTURE_CUBE_MAP_SEAMLESS = 0x884F
GL_POINT_SPRITE = 0x8861
GL_COORD_REPLACE = 0x8862
GL_QUERY_COUNTER_BITS = 0x8864
GL_CURRENT_QUERY = 0x8865
GL_QUERY_RESULT = 0x8866
GL_QUERY_RESULT_AVAILABLE = 0x8867
GL_MAX_VERTEX_ATTRIBS = 0x8869
GL_VERTEX_ATTRIB_ARRAY_NORMALIZED = 0x886A
GL_MAX_TESS_CONTROL_INPUT_COMPONENTS = 0x886C
GL_MAX_TESS_EVALUATION_INPUT_COMPONENTS = 0x886D
GL_MAX_TEXTURE_COORDS = 0x8871
GL_MAX_TEXTURE_IMAGE_UNITS = 0x8872
GL_GEOMETRY_SHADER_INVOCATIONS = 0x887F
GL_ARRAY_BUFFER = 0x8892
GL_ELEMENT_ARRAY_BUFFER = 0x8893
GL_ARRAY_BUFFER_BINDING = 0x8894
GL_ELEMENT_ARRAY_BUFFER_BINDING = 0x8895
GL_VERTEX_ARRAY_BUFFER_BINDING = 0x8896
GL_NORMAL_ARRAY_BUFFER_BINDING = 0x8897
GL_COLOR_ARRAY_BUFFER_BINDING = 0x8898
GL_INDEX_ARRAY_BUFFER_BINDING = 0x8899
GL_TEXTURE_COORD_ARRAY_BUFFER_BINDING = 0x889A
GL_EDGE_FLAG_ARRAY_BUFFER_BINDING = 0x889B
GL_SECONDARY_COLOR_ARRAY_BUFFER_BINDING = 0x889C
GL_FOG_COORD_ARRAY_BUFFER_BINDING = 0x889D
GL_FOG_COORDINATE_ARRAY_BUFFER_BINDING = 0x889D
GL_WEIGHT_ARRAY_BUFFER_BINDING = 0x889E
GL_VERTEX_ATTRIB_ARRAY_BUFFER_BINDING = 0x889F
GL_READ_ONLY = 0x88B8
GL_WRITE_ONLY = 0x88B9
GL_READ_WRITE = 0x88BA
GL_BUFFER_ACCESS = 0x88BB
GL_BUFFER_MAPPED = 0x88BC
GL_BUFFER_MAP_POINTER = 0x88BD
GL_TIME_ELAPSED = 0x88BF
GL_STREAM_DRAW = 0x88E0
GL_STREAM_READ = 0x88E1
GL_STREAM_COPY = 0x88E2
GL_STATIC_DRAW = 0x88E4
GL_STATIC_READ = 0x88E5
GL_STATIC_COPY = 0x88E6
GL_DYNAMIC_DRAW = 0x88E8
GL_DYNAMIC_READ = 0x88E9
GL_DYNAMIC_COPY = 0x88EA
GL_PIXEL_PACK_BUFFER = 0x88EB
GL_PIXEL_UNPACK_BUFFER = 0x88EC
GL_PIXEL_PACK_BUFFER_BINDING = 0x88ED
GL_PIXEL_UNPACK_BUFFER_BINDING = 0x88EF
GL_DEPTH24_STENCIL8 = 0x88F0
GL_TEXTURE_STENCIL_SIZE = 0x88F1
GL_SRC1_COLOR = 0x88F9
GL_ONE_MINUS_SRC1_COLOR = 0x88FA
GL_ONE_MINUS_SRC1_ALPHA = 0x88FB
GL_MAX_DUAL_SOURCE_DRAW_BUFFERS = 0x88FC
GL_VERTEX_ATTRIB_ARRAY_INTEGER = 0x88FD
GL_VERTEX_ATTRIB_ARRAY_DIVISOR = 0x88FE
GL_VERTEX_ATTRIB_ARRAY_DIVISOR_ANGLE = 0x88FE
GL_MAX_ARRAY_TEXTURE_LAYERS = 0x88FF
GL_MIN_PROGRAM_TEXEL_OFFSET = 0x8904
GL_MAX_PROGRAM_TEXEL_OFFSET = 0x8905
GL_SAMPLES_PASSED = 0x8914
GL_GEOMETRY_VERTICES_OUT = 0x8916
GL_GEOMETRY_INPUT_TYPE = 0x8917
GL_GEOMETRY_OUTPUT_TYPE = 0x8918
GL_SAMPLER_BINDING = 0x8919
GL_CLAMP_VERTEX_COLOR = 0x891A
GL_CLAMP_FRAGMENT_COLOR = 0x891B
GL_CLAMP_READ_COLOR = 0x891C
GL_FIXED_ONLY = 0x891D
GL_UNIFORM_BUFFER = 0x8A11
GL_UNIFORM_BUFFER_BINDING = 0x8A28
GL_UNIFORM_BUFFER_START = 0x8A29
GL_UNIFORM_BUFFER_SIZE = 0x8A2A
GL_MAX_VERTEX_UNIFORM_BLOCKS = 0x8A2B
GL_MAX_GEOMETRY_UNIFORM_BLOCKS = 0x8A2C
GL_MAX_FRAGMENT_UNIFORM_BLOCKS = 0x8A2D
GL_MAX_COMBINED_UNIFORM_BLOCKS = 0x8A2E
GL_MAX_UNIFORM_BUFFER_BINDINGS = 0x8A2F
GL_MAX_UNIFORM_BLOCK_SIZE = 0x8A30
GL_MAX_COMBINED_VERTEX_UNIFORM_COMPONENTS = 0x8A31
GL_MAX_COMBINED_GEOMETRY_UNIFORM_COMPONENTS = 0x8A32
GL_MAX_COMBINED_FRAGMENT_UNIFORM_COMPONENTS = 0x8A33
GL_UNIFORM_BUFFER_OFFSET_ALIGNMENT = 0x8A34
GL_ACTIVE_UNIFORM_BLOCK_MAX_NAME_LENGTH = 0x8A35
GL_ACTIVE_UNIFORM_BLOCKS = 0x8A36
GL_UNIFORM_TYPE = 0x8A37
GL_UNIFORM_SIZE = 0x8A38
GL_UNIFORM_NAME_LENGTH = 0x8A39
GL_UNIFORM_BLOCK_INDEX = 0x8A3A
GL_UNIFORM_OFFSET = 0x8A3B
GL_UNIFORM_ARRAY_STRIDE = 0x8A3C
GL_UNIFORM_MATRIX_STRIDE = 0x8A3D
GL_UNIFORM_IS_ROW_MAJOR = 0x8A3E
GL_UNIFORM_BLOCK_BINDING = 0x8A3F
GL_UNIFORM_BLOCK_DATA_SIZE = 0x8A40
GL_UNIFORM_BLOCK_NAME_LENGTH = 0x8A41
GL_UNIFORM_BLOCK_ACTIVE_UNIFORMS = 0x8A42
GL_UNIFORM_BLOCK_ACTIVE_UNIFORM_INDICES = 0x8A43
GL_UNIFORM_BLOCK_REFERENCED_BY_VERTEX_SHADER = 0x8A44
GL_UNIFORM_BLOCK_REFERENCED_BY_GEOMETRY_SHADER = 0x8A45
GL_UNIFORM_BLOCK_REFERENCED_BY_FRAGMENT_SHADER = 0x8A46
GL_SAMPLER_2D_RECT = 0x8B63
GL_SAMPLER_2D_RECT_SHADOW = 0x8B64
GL_FRAGMENT_SHADER = 0x8B30
GL_VERTEX_SHADER = 0x8B31
GL_MAX_FRAGMENT_UNIFORM_COMPONENTS = 0x8B49
GL_MAX_VERTEX_UNIFORM_COMPONENTS = 0x8B4A
GL_MAX_VARYING_FLOATS = 0x8B4B
GL_MAX_VERTEX_TEXTURE_IMAGE_UNITS = 0x8B4C
GL_MAX_COMBINED_TEXTURE_IMAGE_UNITS = 0x8B4D
GL_SHADER_TYPE = 0x8B4F
GL_FLOAT_VEC2 = 0x8B50
GL_FLOAT_VEC3 = 0x8B51
GL_FLOAT_VEC4 = 0x8B52
GL_INT_VEC2 = 0x8B53
GL_INT_VEC3 = 0x8B54
GL_INT_VEC4 = 0x8B55
GL_BOOL = 0x8B56
GL_BOOL_VEC2 = 0x8B57
GL_BOOL_VEC3 = 0x8B58
GL_BOOL_VEC4 = 0x8B59
GL_FLOAT_MAT2 = 0x8B5A
GL_FLOAT_MAT3 = 0x8B5B
GL_FLOAT_MAT4 = 0x8B5C
GL_SAMPLER_1D = 0x8B5D
GL_SAMPLER_2D = 0x8B5E
GL_SAMPLER_3D = 0x8B5F
GL_SAMPLER_CUBE = 0x8B60
GL_SAMPLER_1D_SHADOW = 0x8B61
GL_SAMPLER_2D_SHADOW = 0x8B62
GL_DELETE_STATUS = 0x8B80
GL_COMPILE_STATUS = 0x8B81
GL_LINK_STATUS = 0x8B82
GL_VALIDATE_STATUS = 0x8B83
GL_INFO_LOG_LENGTH = 0x8B84
GL_ATTACHED_SHADERS = 0x8B85
GL_ACTIVE_UNIFORMS = 0x8B86
GL_ACTIVE_UNIFORM_MAX_LENGTH = 0x8B87
GL_SHADER_SOURCE_LENGTH = 0x8B88
GL_ACTIVE_ATTRIBUTES = 0x8B89
GL_ACTIVE_ATTRIBUTE_MAX_LENGTH = 0x8B8A
GL_FRAGMENT_SHADER_DERIVATIVE_HINT = 0x8B8B
GL_SHADING_LANGUAGE_VERSION = 0x8B8C
GL_MAX_VARYING_COMPONENTS = 0x8B4B
GL_CURRENT_PROGRAM = 0x8B8D
GL_IMPLEMENTATION_COLOR_READ_TYPE = 0x8B9A
GL_IMPLEMENTATION_COLOR_READ_FORMAT = 0x8B9B
GL_STATE_RESTORE = 0x8BDC
GL_COMPRESSED_RGB_PVRTC_4BPPV1_IMG = 0x8C00
GL_COMPRESSED_RGB_PVRTC_2BPPV1_IMG = 0x8C01
GL_COMPRESSED_RGBA_PVRTC_4BPPV1_IMG = 0x8C02
GL_COMPRESSED_RGBA_PVRTC_2BPPV1_IMG = 0x8C03
GL_MODULATE_COLOR_IMG = 0x8C04
GL_RECIP_ADD_SIGNED_ALPHA_IMG = 0x8C05
GL_TEXTURE_ALPHA_MODULATE_IMG = 0x8C06
GL_FACTOR_ALPHA_MODULATE_IMG = 0x8C07
GL_FRAGMENT_ALPHA_MODULATE_IMG = 0x8C08
GL_ADD_BLEND_IMG = 0x8C09
GL_SGX_BINARY_IMG = 0x8C0A
GL_TEXTURE_RED_TYPE = 0x8C10
GL_TEXTURE_GREEN_TYPE = 0x8C11
GL_TEXTURE_BLUE_TYPE = 0x8C12
GL_TEXTURE_ALPHA_TYPE = 0x8C13
GL_TEXTURE_LUMINANCE_TYPE = 0x8C14
GL_TEXTURE_INTENSITY_TYPE = 0x8C15
GL_TEXTURE_DEPTH_TYPE = 0x8C16
GL_UNSIGNED_NORMALIZED = 0x8C17
GL_TEXTURE_1D_ARRAY = 0x8C18
GL_PROXY_TEXTURE_1D_ARRAY = 0x8C19
GL_TEXTURE_2D_ARRAY = 0x8C1A
GL_PROXY_TEXTURE_2D_ARRAY = 0x8C1B
GL_TEXTURE_BINDING_1D_ARRAY = 0x8C1C
GL_TEXTURE_BINDING_2D_ARRAY = 0x8C1D
GL_MAX_GEOMETRY_TEXTURE_IMAGE_UNITS = 0x8C29
GL_TEXTURE_BUFFER = 0x8C2A
GL_MAX_TEXTURE_BUFFER_SIZE = 0x8C2B
GL_TEXTURE_BINDING_BUFFER = 0x8C2C
GL_TEXTURE_BUFFER_DATA_STORE_BINDING = 0x8C2D
GL_ANY_SAMPLES_PASSED = 0x8C2F
GL_R11F_G11F_B10F = 0x8C3A
GL_UNSIGNED_INT_10F_11F_11F_REV = 0x8C3B
GL_RGB9_E5 = 0x8C3D
GL_UNSIGNED_INT_5_9_9_9_REV = 0x8C3E
GL_TEXTURE_SHARED_SIZE = 0x8C3F
GL_SRGB = 0x8C40
GL_SRGB8 = 0x8C41
GL_SRGB_ALPHA = 0x8C42
GL_SRGB8_ALPHA8 = 0x8C43
GL_SLUMINANCE_ALPHA = 0x8C44
GL_SLUMINANCE8_ALPHA8 = 0x8C45
GL_SLUMINANCE = 0x8C46
GL_SLUMINANCE8 = 0x8C47
GL_COMPRESSED_SRGB = 0x8C48
GL_COMPRESSED_SRGB_ALPHA = 0x8C49
GL_COMPRESSED_SLUMINANCE = 0x8C4A
GL_COMPRESSED_SLUMINANCE_ALPHA = 0x8C4B
GL_TRANSFORM_FEEDBACK_VARYING_MAX_LENGTH = 0x8C76
GL_TRANSFORM_FEEDBACK_BUFFER_MODE = 0x8C7F
GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_COMPONENTS = 0x8C80
GL_TRANSFORM_FEEDBACK_VARYINGS = 0x8C83
GL_TRANSFORM_FEEDBACK_BUFFER_START = 0x8C84
GL_TRANSFORM_FEEDBACK_BUFFER_SIZE = 0x8C85
GL_PRIMITIVES_GENERATED = 0x8C87
GL_TRANSFORM_FEEDBACK_PRIMITIVES_WRITTEN = 0x8C88
GL_RASTERIZER_DISCARD = 0x8C89
GL_MAX_TRANSFORM_FEEDBACK_INTERLEAVED_COMPONENTS = 0x8C8A
GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_ATTRIBS = 0x8C8B
GL_INTERLEAVED_ATTRIBS = 0x8C8C
GL_SEPARATE_ATTRIBS = 0x8C8D
GL_TRANSFORM_FEEDBACK_BUFFER = 0x8C8E
GL_TRANSFORM_FEEDBACK_BUFFER_BINDING = 0x8C8F
GL_POINT_SPRITE_COORD_ORIGIN = 0x8CA0
GL_LOWER_LEFT = 0x8CA1
GL_UPPER_LEFT = 0x8CA2
GL_STENCIL_BACK_REF = 0x8CA3
GL_STENCIL_BACK_VALUE_MASK = 0x8CA4
GL_STENCIL_BACK_WRITEMASK = 0x8CA5
GL_FRAMEBUFFER_BINDING = 0x8CA6
GL_DRAW_FRAMEBUFFER_BINDING = 0x8CA6
GL_RENDERBUFFER_BINDING = 0x8CA7
GL_FRAMEBUFFER_BINDING_ANGLE = 0x8CA6
GL_RENDERBUFFER_BINDING_ANGLE = 0x8CA7
GL_READ_FRAMEBUFFER = 0x8CA8
GL_DRAW_FRAMEBUFFER = 0x8CA9
GL_READ_FRAMEBUFFER_BINDING = 0x8CAA
GL_READ_FRAMEBUFFER_ANGLE = 0x8CA8
GL_DRAW_FRAMEBUFFER_ANGLE = 0x8CA9
GL_RENDERBUFFER_SAMPLES = 0x8CAB
GL_RENDERBUFFER_SAMPLES_ANGLE = 0x8CAB
GL_DEPTH_COMPONENT32F = 0x8CAC
GL_DEPTH32F_STENCIL8 = 0x8CAD
GL_FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE = 0x8CD0
GL_FRAMEBUFFER_ATTACHMENT_OBJECT_NAME = 0x8CD1
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LEVEL = 0x8CD2
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_CUBE_MAP_FACE = 0x8CD3
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LAYER = 0x8CD4
GL_FRAMEBUFFER_COMPLETE = 0x8CD5
GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT = 0x8CD6
GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT = 0x8CD7
GL_FRAMEBUFFER_INCOMPLETE_DRAW_BUFFER = 0x8CDB
GL_FRAMEBUFFER_INCOMPLETE_READ_BUFFER = 0x8CDC
GL_FRAMEBUFFER_UNSUPPORTED = 0x8CDD
GL_MAX_COLOR_ATTACHMENTS = 0x8CDF
GL_COLOR_ATTACHMENT0 = 0x8CE0
GL_COLOR_ATTACHMENT1 = 0x8CE1
GL_COLOR_ATTACHMENT2 = 0x8CE2
GL_COLOR_ATTACHMENT3 = 0x8CE3
GL_COLOR_ATTACHMENT4 = 0x8CE4
GL_COLOR_ATTACHMENT5 = 0x8CE5
GL_COLOR_ATTACHMENT6 = 0x8CE6
GL_COLOR_ATTACHMENT7 = 0x8CE7
GL_COLOR_ATTACHMENT8 = 0x8CE8
GL_COLOR_ATTACHMENT9 = 0x8CE9
GL_COLOR_ATTACHMENT10 = 0x8CEA
GL_COLOR_ATTACHMENT11 = 0x8CEB
GL_COLOR_ATTACHMENT12 = 0x8CEC
GL_COLOR_ATTACHMENT13 = 0x8CED
GL_COLOR_ATTACHMENT14 = 0x8CEE
GL_COLOR_ATTACHMENT15 = 0x8CEF
GL_DEPTH_ATTACHMENT = 0x8D00
GL_STENCIL_ATTACHMENT = 0x8D20
GL_FRAMEBUFFER = 0x8D40
GL_RENDERBUFFER = 0x8D41
GL_RENDERBUFFER_WIDTH = 0x8D42
GL_RENDERBUFFER_HEIGHT = 0x8D43
GL_RENDERBUFFER_INTERNAL_FORMAT = 0x8D44
GL_STENCIL_INDEX1 = 0x8D46
GL_STENCIL_INDEX4 = 0x8D47
GL_STENCIL_INDEX8 = 0x8D48
GL_STENCIL_INDEX16 = 0x8D49
GL_RENDERBUFFER_RED_SIZE = 0x8D50
GL_RENDERBUFFER_GREEN_SIZE = 0x8D51
GL_RENDERBUFFER_BLUE_SIZE = 0x8D52
GL_RENDERBUFFER_ALPHA_SIZE = 0x8D53
GL_RENDERBUFFER_DEPTH_SIZE = 0x8D54
GL_RENDERBUFFER_STENCIL_SIZE = 0x8D55
GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE = 0x8D56
GL_MAX_SAMPLES = 0x8D57
GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE_ANGLE = 0x8D56
GL_MAX_SAMPLES_ANGLE = 0x8D57
GL_RGB565 = 0x8D62
GL_PRIMITIVE_RESTART_FIXED_INDEX = 0x8D69
GL_ANY_SAMPLES_PASSED_CONSERVATIVE = 0x8D6A
GL_MAX_ELEMENT_INDEX = 0x8D6B
GL_RGBA32UI = 0x8D70
GL_RGB32UI = 0x8D71
GL_RGBA16UI = 0x8D76
GL_RGB16UI = 0x8D77
GL_RGBA8UI = 0x8D7C
GL_RGB8UI = 0x8D7D
GL_RGBA32I = 0x8D82
GL_RGB32I = 0x8D83
GL_RGBA16I = 0x8D88
GL_RGB16I = 0x8D89
GL_RGBA8I = 0x8D8E
GL_RGB8I = 0x8D8F
GL_RED_INTEGER = 0x8D94
GL_GREEN_INTEGER = 0x8D95
GL_BLUE_INTEGER = 0x8D96
GL_ALPHA_INTEGER = 0x8D97
GL_RGB_INTEGER = 0x8D98
GL_RGBA_INTEGER = 0x8D99
GL_BGR_INTEGER = 0x8D9A
GL_BGRA_INTEGER = 0x8D9B
GL_INT_2_10_10_10_REV = 0x8D9F
GL_FRAMEBUFFER_ATTACHMENT_LAYERED = 0x8DA7
GL_FRAMEBUFFER_INCOMPLETE_LAYER_TARGETS = 0x8DA8
GL_FLOAT_32_UNSIGNED_INT_24_8_REV = 0x8DAD
GL_FRAMEBUFFER_SRGB = 0x8DB9
GL_COMPRESSED_RED_RGTC1 = 0x8DBB
GL_COMPRESSED_SIGNED_RED_RGTC1 = 0x8DBC
GL_COMPRESSED_RG_RGTC2 = 0x8DBD
GL_COMPRESSED_SIGNED_RG_RGTC2 = 0x8DBE
GL_SAMPLER_1D_ARRAY = 0x8DC0
GL_SAMPLER_2D_ARRAY = 0x8DC1
GL_SAMPLER_1D_ARRAY_SHADOW = 0x8DC3
GL_SAMPLER_2D_ARRAY_SHADOW = 0x8DC4
GL_SAMPLER_CUBE_SHADOW = 0x8DC5
GL_UNSIGNED_INT_VEC2 = 0x8DC6
GL_UNSIGNED_INT_VEC3 = 0x8DC7
GL_UNSIGNED_INT_VEC4 = 0x8DC8
GL_INT_SAMPLER_1D = 0x8DC9
GL_INT_SAMPLER_2D = 0x8DCA
GL_INT_SAMPLER_3D = 0x8DCB
GL_INT_SAMPLER_CUBE = 0x8DCC
GL_INT_SAMPLER_1D_ARRAY = 0x8DCE
GL_INT_SAMPLER_2D_ARRAY = 0x8DCF
GL_UNSIGNED_INT_SAMPLER_1D = 0x8DD1
GL_UNSIGNED_INT_SAMPLER_2D = 0x8DD2
GL_UNSIGNED_INT_SAMPLER_3D = 0x8DD3
GL_UNSIGNED_INT_SAMPLER_CUBE = 0x8DD4
GL_UNSIGNED_INT_SAMPLER_1D_ARRAY = 0x8DD6
GL_UNSIGNED_INT_SAMPLER_2D_ARRAY = 0x8DD7
GL_SAMPLER_BUFFER = 0x8DC2
GL_INT_SAMPLER_2D_RECT = 0x8DCD
GL_INT_SAMPLER_BUFFER = 0x8DD0
GL_UNSIGNED_INT_SAMPLER_2D_RECT = 0x8DD5
GL_UNSIGNED_INT_SAMPLER_BUFFER = 0x8DD8
GL_GEOMETRY_SHADER = 0x8DD9
GL_MAX_GEOMETRY_UNIFORM_COMPONENTS = 0x8DDF
GL_MAX_GEOMETRY_OUTPUT_VERTICES = 0x8DE0
GL_MAX_GEOMETRY_TOTAL_OUTPUT_COMPONENTS = 0x8DE1
GL_ACTIVE_SUBROUTINES = 0x8DE5
GL_ACTIVE_SUBROUTINE_UNIFORMS = 0x8DE6
GL_MAX_SUBROUTINES = 0x8DE7
GL_MAX_SUBROUTINE_UNIFORM_LOCATIONS = 0x8DE8
GL_LOW_FLOAT = 0x8DF0
GL_MEDIUM_FLOAT = 0x8DF1
GL_HIGH_FLOAT = 0x8DF2
GL_LOW_INT = 0x8DF3
GL_MEDIUM_INT = 0x8DF4
GL_HIGH_INT = 0x8DF5
GL_SHADER_BINARY_FORMATS = 0x8DF8
GL_NUM_SHADER_BINARY_FORMATS = 0x8DF9
GL_SHADER_COMPILER = 0x8DFA
GL_MAX_VERTEX_UNIFORM_VECTORS = 0x8DFB
GL_MAX_VARYING_VECTORS = 0x8DFC
GL_MAX_FRAGMENT_UNIFORM_VECTORS = 0x8DFD
GL_QUERY_WAIT = 0x8E13
GL_QUERY_NO_WAIT = 0x8E14
GL_QUERY_BY_REGION_WAIT = 0x8E15
GL_QUERY_BY_REGION_NO_WAIT = 0x8E16
GL_MAX_COMBINED_TESS_CONTROL_UNIFORM_COMPONENTS = 0x8E1E
GL_MAX_COMBINED_TESS_EVALUATION_UNIFORM_COMPONENTS = 0x8E1F
GL_TRANSFORM_FEEDBACK = 0x8E22
GL_TRANSFORM_FEEDBACK_PAUSED = 0x8E23
GL_TRANSFORM_FEEDBACK_ACTIVE = 0x8E24
GL_TRANSFORM_FEEDBACK_BINDING = 0x8E25
GL_TIMESTAMP = 0x8E28
GL_TEXTURE_SWIZZLE_R = 0x8E42
GL_TEXTURE_SWIZZLE_G = 0x8E43
GL_TEXTURE_SWIZZLE_B = 0x8E44
GL_TEXTURE_SWIZZLE_A = 0x8E45
GL_TEXTURE_SWIZZLE_RGBA = 0x8E46
GL_ACTIVE_SUBROUTINE_UNIFORM_LOCATIONS = 0x8E47
GL_ACTIVE_SUBROUTINE_MAX_LENGTH = 0x8E48
GL_ACTIVE_SUBROUTINE_UNIFORM_MAX_LENGTH = 0x8E49
GL_NUM_COMPATIBLE_SUBROUTINES = 0x8E4A
GL_COMPATIBLE_SUBROUTINES = 0x8E4B
GL_QUADS_FOLLOW_PROVOKING_VERTEX_CONVENTION = 0x8E4C
GL_FIRST_VERTEX_CONVENTION = 0x8E4D
GL_LAST_VERTEX_CONVENTION = 0x8E4E
GL_PROVOKING_VERTEX = 0x8E4F
GL_SAMPLE_POSITION = 0x8E50
GL_SAMPLE_MASK = 0x8E51
GL_SAMPLE_MASK_VALUE = 0x8E52
GL_MAX_SAMPLE_MASK_WORDS = 0x8E59
GL_MAX_GEOMETRY_SHADER_INVOCATIONS = 0x8E5A
GL_MIN_FRAGMENT_INTERPOLATION_OFFSET = 0x8E5B
GL_MAX_FRAGMENT_INTERPOLATION_OFFSET = 0x8E5C
GL_FRAGMENT_INTERPOLATION_OFFSET_BITS = 0x8E5D
GL_MIN_PROGRAM_TEXTURE_GATHER_OFFSET = 0x8E5E
GL_MAX_PROGRAM_TEXTURE_GATHER_OFFSET = 0x8E5F
GL_MAX_TRANSFORM_FEEDBACK_BUFFERS = 0x8E70
GL_MAX_VERTEX_STREAMS = 0x8E71
GL_PATCH_VERTICES = 0x8E72
GL_PATCH_DEFAULT_INNER_LEVEL = 0x8E73
GL_PATCH_DEFAULT_OUTER_LEVEL = 0x8E74
GL_TESS_CONTROL_OUTPUT_VERTICES = 0x8E75
GL_TESS_GEN_MODE = 0x8E76
GL_TESS_GEN_SPACING = 0x8E77
GL_TESS_GEN_VERTEX_ORDER = 0x8E78
GL_TESS_GEN_POINT_MODE = 0x8E79
GL_ISOLINES = 0x8E7A
GL_FRACTIONAL_ODD = 0x8E7B
GL_FRACTIONAL_EVEN = 0x8E7C
GL_MAX_PATCH_VERTICES = 0x8E7D
GL_MAX_TESS_GEN_LEVEL = 0x8E7E
GL_MAX_TESS_CONTROL_UNIFORM_COMPONENTS = 0x8E7F
GL_MAX_TESS_EVALUATION_UNIFORM_COMPONENTS = 0x8E80
GL_MAX_TESS_CONTROL_TEXTURE_IMAGE_UNITS = 0x8E81
GL_MAX_TESS_EVALUATION_TEXTURE_IMAGE_UNITS = 0x8E82
GL_MAX_TESS_CONTROL_OUTPUT_COMPONENTS = 0x8E83
GL_MAX_TESS_PATCH_COMPONENTS = 0x8E84
GL_MAX_TESS_CONTROL_TOTAL_OUTPUT_COMPONENTS = 0x8E85
GL_MAX_TESS_EVALUATION_OUTPUT_COMPONENTS = 0x8E86
GL_TESS_EVALUATION_SHADER = 0x8E87
GL_TESS_CONTROL_SHADER = 0x8E88
GL_MAX_TESS_CONTROL_UNIFORM_BLOCKS = 0x8E89
GL_MAX_TESS_EVALUATION_UNIFORM_BLOCKS = 0x8E8A
GL_COPY_READ_BUFFER_BINDING = 0x8F36
GL_COPY_WRITE_BUFFER_BINDING = 0x8F37
GL_MAX_IMAGE_UNITS = 0x8F38
GL_MAX_COMBINED_IMAGE_UNITS_AND_FRAGMENT_OUTPUTS = 0x8F39
GL_IMAGE_BINDING_NAME = 0x8F3A
GL_IMAGE_BINDING_LEVEL = 0x8F3B
GL_IMAGE_BINDING_LAYERED = 0x8F3C
GL_IMAGE_BINDING_LAYER = 0x8F3D
GL_IMAGE_BINDING_ACCESS = 0x8F3E
GL_DRAW_INDIRECT_BUFFER = 0x8F3F
GL_DRAW_INDIRECT_BUFFER_BINDING = 0x8F43
GL_DOUBLE_MAT2 = 0x8F46
GL_DOUBLE_MAT3 = 0x8F47
GL_DOUBLE_MAT4 = 0x8F48
GL_RED_SNORM = 0x8F90
GL_RG_SNORM = 0x8F91
GL_RGB_SNORM = 0x8F92
GL_RGBA_SNORM = 0x8F93
GL_R8_SNORM = 0x8F94
GL_RG8_SNORM = 0x8F95
GL_RGB8_SNORM = 0x8F96
GL_RGBA8_SNORM = 0x8F97
GL_R16_SNORM = 0x8F98
GL_RG16_SNORM = 0x8F99
GL_RGB16_SNORM = 0x8F9A
GL_RGBA16_SNORM = 0x8F9B
GL_SIGNED_NORMALIZED = 0x8F9C
GL_PRIMITIVE_RESTART = 0x8F9D
GL_PRIMITIVE_RESTART_INDEX = 0x8F9E
GL_MAX_PROGRAM_TEXTURE_GATHER_COMPONENTS = 0x8F9F
GL_SHADER_BINARY_VIV = 0x8FC4
GL_DOUBLE_VEC2 = 0x8FFC
GL_DOUBLE_VEC3 = 0x8FFD
GL_DOUBLE_VEC4 = 0x8FFE
GL_TEXTURE_CUBE_MAP_ARRAY = 0x9009
GL_TEXTURE_BINDING_CUBE_MAP_ARRAY = 0x900A
GL_PROXY_TEXTURE_CUBE_MAP_ARRAY = 0x900B
GL_SAMPLER_CUBE_MAP_ARRAY = 0x900C
GL_SAMPLER_CUBE_MAP_ARRAY_SHADOW = 0x900D
GL_INT_SAMPLER_CUBE_MAP_ARRAY = 0x900E
GL_UNSIGNED_INT_SAMPLER_CUBE_MAP_ARRAY = 0x900F
GL_ALPHA_SNORM = 0x9010
GL_LUMINANCE_SNORM = 0x9011
GL_LUMINANCE_ALPHA_SNORM = 0x9012
GL_INTENSITY_SNORM = 0x9013
GL_ALPHA8_SNORM = 0x9014
GL_LUMINANCE8_SNORM = 0x9015
GL_LUMINANCE8_ALPHA8_SNORM = 0x9016
GL_INTENSITY8_SNORM = 0x9017
GL_ALPHA16_SNORM = 0x9018
GL_LUMINANCE16_SNORM = 0x9019
GL_LUMINANCE16_ALPHA16_SNORM = 0x901A
GL_INTENSITY16_SNORM = 0x901B
GL_IMAGE_1D = 0x904C
GL_IMAGE_2D = 0x904D
GL_IMAGE_3D = 0x904E
GL_IMAGE_2D_RECT = 0x904F
GL_IMAGE_CUBE = 0x9050
GL_IMAGE_BUFFER = 0x9051
GL_IMAGE_1D_ARRAY = 0x9052
GL_IMAGE_2D_ARRAY = 0x9053
GL_IMAGE_CUBE_MAP_ARRAY = 0x9054
GL_IMAGE_2D_MULTISAMPLE = 0x9055
GL_IMAGE_2D_MULTISAMPLE_ARRAY = 0x9056
GL_INT_IMAGE_1D = 0x9057
GL_INT_IMAGE_2D = 0x9058
GL_INT_IMAGE_3D = 0x9059
GL_INT_IMAGE_2D_RECT = 0x905A
GL_INT_IMAGE_CUBE = 0x905B
GL_INT_IMAGE_BUFFER = 0x905C
GL_INT_IMAGE_1D_ARRAY = 0x905D
GL_INT_IMAGE_2D_ARRAY = 0x905E
GL_INT_IMAGE_CUBE_MAP_ARRAY = 0x905F
GL_INT_IMAGE_2D_MULTISAMPLE = 0x9060
GL_INT_IMAGE_2D_MULTISAMPLE_ARRAY = 0x9061
GL_UNSIGNED_INT_IMAGE_1D = 0x9062
GL_UNSIGNED_INT_IMAGE_2D = 0x9063
GL_UNSIGNED_INT_IMAGE_3D = 0x9064
GL_UNSIGNED_INT_IMAGE_2D_RECT = 0x9065
GL_UNSIGNED_INT_IMAGE_CUBE = 0x9066
GL_UNSIGNED_INT_IMAGE_BUFFER = 0x9067
GL_UNSIGNED_INT_IMAGE_1D_ARRAY = 0x9068
GL_UNSIGNED_INT_IMAGE_2D_ARRAY = 0x9069
GL_UNSIGNED_INT_IMAGE_CUBE_MAP_ARRAY = 0x906A
GL_UNSIGNED_INT_IMAGE_2D_MULTISAMPLE = 0x906B
GL_UNSIGNED_INT_IMAGE_2D_MULTISAMPLE_ARRAY = 0x906C
GL_MAX_IMAGE_SAMPLES = 0x906D
GL_IMAGE_BINDING_FORMAT = 0x906E
GL_RGB10_A2UI = 0x906F
GL_MIN_MAP_BUFFER_ALIGNMENT = 0x90BC
GL_IMAGE_FORMAT_COMPATIBILITY_TYPE = 0x90C7
GL_IMAGE_FORMAT_COMPATIBILITY_BY_SIZE = 0x90C8
GL_IMAGE_FORMAT_COMPATIBILITY_BY_CLASS = 0x90C9
GL_MAX_VERTEX_IMAGE_UNIFORMS = 0x90CA
GL_MAX_TESS_CONTROL_IMAGE_UNIFORMS = 0x90CB
GL_MAX_TESS_EVALUATION_IMAGE_UNIFORMS = 0x90CC
GL_MAX_GEOMETRY_IMAGE_UNIFORMS = 0x90CD
GL_MAX_FRAGMENT_IMAGE_UNIFORMS = 0x90CE
GL_MAX_COMBINED_IMAGE_UNIFORMS = 0x90CF
GL_SHADER_STORAGE_BUFFER = 0x90D2
GL_SHADER_STORAGE_BUFFER_BINDING = 0x90D3
GL_SHADER_STORAGE_BUFFER_START = 0x90D4
GL_SHADER_STORAGE_BUFFER_SIZE = 0x90D5
GL_MAX_VERTEX_SHADER_STORAGE_BLOCKS = 0x90D6
GL_MAX_GEOMETRY_SHADER_STORAGE_BLOCKS = 0x90D7
GL_MAX_TESS_CONTROL_SHADER_STORAGE_BLOCKS = 0x90D8
GL_MAX_TESS_EVALUATION_SHADER_STORAGE_BLOCKS = 0x90D9
GL_MAX_FRAGMENT_SHADER_STORAGE_BLOCKS = 0x90DA
GL_MAX_COMPUTE_SHADER_STORAGE_BLOCKS = 0x90DB
GL_MAX_COMBINED_SHADER_STORAGE_BLOCKS = 0x90DC
GL_MAX_SHADER_STORAGE_BUFFER_BINDINGS = 0x90DD
GL_MAX_SHADER_STORAGE_BLOCK_SIZE = 0x90DE
GL_SHADER_STORAGE_BUFFER_OFFSET_ALIGNMENT = 0x90DF
GL_DEPTH_STENCIL_TEXTURE_MODE = 0x90EA
GL_MAX_COMPUTE_LOCAL_INVOCATIONS = 0x90EB
GL_UNIFORM_BLOCK_REFERENCED_BY_COMPUTE_SHADER = 0x90EC
GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_COMPUTE_SHADER = 0x90ED
GL_DISPATCH_INDIRECT_BUFFER = 0x90EE
GL_DISPATCH_INDIRECT_BUFFER_BINDING = 0x90EF
GL_TEXTURE_2D_MULTISAMPLE = 0x9100
GL_PROXY_TEXTURE_2D_MULTISAMPLE = 0x9101
GL_TEXTURE_2D_MULTISAMPLE_ARRAY = 0x9102
GL_PROXY_TEXTURE_2D_MULTISAMPLE_ARRAY = 0x9103
GL_TEXTURE_BINDING_2D_MULTISAMPLE = 0x9104
GL_TEXTURE_BINDING_2D_MULTISAMPLE_ARRAY = 0x9105
GL_TEXTURE_SAMPLES = 0x9106
GL_TEXTURE_FIXED_SAMPLE_LOCATIONS = 0x9107
GL_SAMPLER_2D_MULTISAMPLE = 0x9108
GL_INT_SAMPLER_2D_MULTISAMPLE = 0x9109
GL_UNSIGNED_INT_SAMPLER_2D_MULTISAMPLE = 0x910A
GL_SAMPLER_2D_MULTISAMPLE_ARRAY = 0x910B
GL_INT_SAMPLER_2D_MULTISAMPLE_ARRAY = 0x910C
GL_UNSIGNED_INT_SAMPLER_2D_MULTISAMPLE_ARRAY = 0x910D
GL_MAX_COLOR_TEXTURE_SAMPLES = 0x910E
GL_MAX_DEPTH_TEXTURE_SAMPLES = 0x910F
GL_MAX_INTEGER_SAMPLES = 0x9110
GL_MAX_SERVER_WAIT_TIMEOUT = 0x9111
GL_OBJECT_TYPE = 0x9112
GL_SYNC_CONDITION = 0x9113
GL_SYNC_STATUS = 0x9114
GL_SYNC_FLAGS = 0x9115
GL_SYNC_FENCE = 0x9116
GL_SYNC_GPU_COMMANDS_COMPLETE = 0x9117
GL_UNSIGNALED = 0x9118
GL_SIGNALED = 0x9119
GL_ALREADY_SIGNALED = 0x911A
GL_TIMEOUT_EXPIRED = 0x911B
GL_CONDITION_SATISFIED = 0x911C
GL_WAIT_FAILED = 0x911D
GL_SYNC_FLUSH_COMMANDS_BIT = 0x00000001
GL_BUFFER_ACCESS_FLAGS = 0x911F
GL_BUFFER_MAP_LENGTH = 0x9120
GL_BUFFER_MAP_OFFSET = 0x9121
GL_MAX_VERTEX_OUTPUT_COMPONENTS = 0x9122
GL_MAX_GEOMETRY_INPUT_COMPONENTS = 0x9123
GL_MAX_GEOMETRY_OUTPUT_COMPONENTS = 0x9124
GL_MAX_FRAGMENT_INPUT_COMPONENTS = 0x9125
GL_CONTEXT_CORE_PROFILE_BIT = 0x00000001
GL_CONTEXT_COMPATIBILITY_PROFILE_BIT = 0x00000002
GL_CONTEXT_PROFILE_MASK = 0x9126
GL_UNPACK_COMPRESSED_BLOCK_WIDTH = 0x9127
GL_UNPACK_COMPRESSED_BLOCK_HEIGHT = 0x9128
GL_UNPACK_COMPRESSED_BLOCK_DEPTH = 0x9129
GL_UNPACK_COMPRESSED_BLOCK_SIZE = 0x912A
GL_PACK_COMPRESSED_BLOCK_WIDTH = 0x912B
GL_PACK_COMPRESSED_BLOCK_HEIGHT = 0x912C
GL_PACK_COMPRESSED_BLOCK_DEPTH = 0x912D
GL_PACK_COMPRESSED_BLOCK_SIZE = 0x912E
GL_TEXTURE_IMMUTABLE_FORMAT = 0x912F
GL_SGX_PROGRAM_BINARY_IMG = 0x9130
GL_RENDERBUFFER_SAMPLES_IMG = 0x9133
GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE_IMG = 0x9134
GL_MAX_SAMPLES_IMG = 0x9135
GL_TEXTURE_SAMPLES_IMG = 0x9136
GL_MAX_DEBUG_MESSAGE_LENGTH = 0x9143
GL_MAX_DEBUG_LOGGED_MESSAGES = 0x9144
GL_DEBUG_LOGGED_MESSAGES = 0x9145
GL_DEBUG_SEVERITY_HIGH = 0x9146
GL_DEBUG_SEVERITY_MEDIUM = 0x9147
GL_DEBUG_SEVERITY_LOW = 0x9148
GL_MAX_SPARSE_ARRAY_TEXTURE_LAYERS = 0x919A
GL_TEXTURE_BUFFER_OFFSET = 0x919D
GL_TEXTURE_BUFFER_SIZE = 0x919E
GL_TEXTURE_BUFFER_OFFSET_ALIGNMENT = 0x919F
GL_COMPUTE_SHADER = 0x91B9
GL_MAX_COMPUTE_UNIFORM_BLOCKS = 0x91BB
GL_MAX_COMPUTE_TEXTURE_IMAGE_UNITS = 0x91BC
GL_MAX_COMPUTE_IMAGE_UNIFORMS = 0x91BD
GL_MAX_COMPUTE_WORK_GROUP_COUNT = 0x91BE
GL_MAX_COMPUTE_WORK_GROUP_SIZE = 0x91BF
GL_SHADER_BINARY_DMP = 0x9250
GL_GCCSO_SHADER_BINARY_FJ = 0x9260
GL_COMPRESSED_R11_EAC = 0x9270
GL_COMPRESSED_SIGNED_R11_EAC = 0x9271
GL_COMPRESSED_RG11_EAC = 0x9272
GL_COMPRESSED_SIGNED_RG11_EAC = 0x9273
GL_COMPRESSED_RGB8_ETC2 = 0x9274
GL_COMPRESSED_SRGB8_ETC2 = 0x9275
GL_COMPRESSED_RGB8_PUNCHTHROUGH_ALPHA1_ETC2 = 0x9276
GL_COMPRESSED_SRGB8_PUNCHTHROUGH_ALPHA1_ETC2 = 0x9277
GL_COMPRESSED_RGBA8_ETC2_EAC = 0x9278
GL_COMPRESSED_SRGB8_ALPHA8_ETC2_EAC = 0x9279
GL_ATOMIC_COUNTER_BUFFER = 0x92C0
GL_ATOMIC_COUNTER_BUFFER_BINDING = 0x92C1
GL_ATOMIC_COUNTER_BUFFER_START = 0x92C2
GL_ATOMIC_COUNTER_BUFFER_SIZE = 0x92C3
GL_ATOMIC_COUNTER_BUFFER_DATA_SIZE = 0x92C4
GL_ATOMIC_COUNTER_BUFFER_ACTIVE_ATOMIC_COUNTERS = 0x92C5
GL_ATOMIC_COUNTER_BUFFER_ACTIVE_ATOMIC_COUNTER_INDICES = 0x92C6
GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_VERTEX_SHADER = 0x92C7
GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_TESS_CONTROL_SHADER = 0x92C8
GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_TESS_EVALUATION_SHADER = 0x92C9
GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_GEOMETRY_SHADER = 0x92CA
GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_FRAGMENT_SHADER = 0x92CB
GL_MAX_VERTEX_ATOMIC_COUNTER_BUFFERS = 0x92CC
GL_MAX_TESS_CONTROL_ATOMIC_COUNTER_BUFFERS = 0x92CD
GL_MAX_TESS_EVALUATION_ATOMIC_COUNTER_BUFFERS = 0x92CE
GL_MAX_GEOMETRY_ATOMIC_COUNTER_BUFFERS = 0x92CF
GL_MAX_FRAGMENT_ATOMIC_COUNTER_BUFFERS = 0x92D0
GL_MAX_COMBINED_ATOMIC_COUNTER_BUFFERS = 0x92D1
GL_MAX_VERTEX_ATOMIC_COUNTERS = 0x92D2
GL_MAX_TESS_CONTROL_ATOMIC_COUNTERS = 0x92D3
GL_MAX_TESS_EVALUATION_ATOMIC_COUNTERS = 0x92D4
GL_MAX_GEOMETRY_ATOMIC_COUNTERS = 0x92D5
GL_MAX_FRAGMENT_ATOMIC_COUNTERS = 0x92D6
GL_MAX_COMBINED_ATOMIC_COUNTERS = 0x92D7
GL_MAX_ATOMIC_COUNTER_BUFFER_SIZE = 0x92D8
GL_MAX_ATOMIC_COUNTER_BUFFER_BINDINGS = 0x92DC
GL_ACTIVE_ATOMIC_COUNTER_BUFFERS = 0x92D9
GL_UNIFORM_ATOMIC_COUNTER_BUFFER_INDEX = 0x92DA
GL_UNSIGNED_INT_ATOMIC_COUNTER = 0x92DB
GL_DEBUG_OUTPUT = 0x92E0
GL_UNIFORM = 0x92E1
GL_UNIFORM_BLOCK = 0x92E2
GL_PROGRAM_INPUT = 0x92E3
GL_PROGRAM_OUTPUT = 0x92E4
GL_BUFFER_VARIABLE = 0x92E5
GL_SHADER_STORAGE_BLOCK = 0x92E6
GL_IS_PER_PATCH = 0x92E7
GL_VERTEX_SUBROUTINE = 0x92E8
GL_TESS_CONTROL_SUBROUTINE = 0x92E9
GL_TESS_EVALUATION_SUBROUTINE = 0x92EA
GL_GEOMETRY_SUBROUTINE = 0x92EB
GL_FRAGMENT_SUBROUTINE = 0x92EC
GL_COMPUTE_SUBROUTINE = 0x92ED
GL_VERTEX_SUBROUTINE_UNIFORM = 0x92EE
GL_TESS_CONTROL_SUBROUTINE_UNIFORM = 0x92EF
GL_TESS_EVALUATION_SUBROUTINE_UNIFORM = 0x92F0
GL_GEOMETRY_SUBROUTINE_UNIFORM = 0x92F1
GL_FRAGMENT_SUBROUTINE_UNIFORM = 0x92F2
GL_COMPUTE_SUBROUTINE_UNIFORM = 0x92F3
GL_TRANSFORM_FEEDBACK_VARYING = 0x92F4
GL_ACTIVE_RESOURCES = 0x92F5
GL_MAX_NAME_LENGTH = 0x92F6
GL_MAX_NUM_ACTIVE_VARIABLES = 0x92F7
GL_MAX_NUM_COMPATIBLE_SUBROUTINES = 0x92F8
GL_NAME_LENGTH = 0x92F9
GL_TYPE = 0x92FA
GL_ARRAY_SIZE = 0x92FB
GL_OFFSET = 0x92FC
GL_BLOCK_INDEX = 0x92FD
GL_ARRAY_STRIDE = 0x92FE
GL_MATRIX_STRIDE = 0x92FF
GL_IS_ROW_MAJOR = 0x9300
GL_ATOMIC_COUNTER_BUFFER_INDEX = 0x9301
GL_BUFFER_BINDING = 0x9302
GL_BUFFER_DATA_SIZE = 0x9303
GL_NUM_ACTIVE_VARIABLES = 0x9304
GL_ACTIVE_VARIABLES = 0x9305
GL_REFERENCED_BY_VERTEX_SHADER = 0x9306
GL_REFERENCED_BY_TESS_CONTROL_SHADER = 0x9307
GL_REFERENCED_BY_TESS_EVALUATION_SHADER = 0x9308
GL_REFERENCED_BY_GEOMETRY_SHADER = 0x9309
GL_REFERENCED_BY_FRAGMENT_SHADER = 0x930A
GL_REFERENCED_BY_COMPUTE_SHADER = 0x930B
GL_TOP_LEVEL_ARRAY_SIZE = 0x930C
GL_TOP_LEVEL_ARRAY_STRIDE = 0x930D
GL_LOCATION = 0x930E
GL_LOCATION_INDEX = 0x930F
GL_FRAMEBUFFER_DEFAULT_WIDTH = 0x9310
GL_FRAMEBUFFER_DEFAULT_HEIGHT = 0x9311
GL_FRAMEBUFFER_DEFAULT_LAYERS = 0x9312
GL_FRAMEBUFFER_DEFAULT_SAMPLES = 0x9313
GL_FRAMEBUFFER_DEFAULT_FIXED_SAMPLE_LOCATIONS = 0x9314
GL_MAX_FRAMEBUFFER_WIDTH = 0x9315
GL_MAX_FRAMEBUFFER_HEIGHT = 0x9316
GL_MAX_FRAMEBUFFER_LAYERS = 0x9317
GL_MAX_FRAMEBUFFER_SAMPLES = 0x9318
GL_NUM_SAMPLE_COUNTS = 0x9380
GL_TRANSLATED_SHADER_SOURCE_LENGTH_ANGLE = 0x93A0
GL_TEXTURE_USAGE_ANGLE = 0x93A2
GL_FRAMEBUFFER_ATTACHMENT_ANGLE = 0x93A3
GL_PACK_REVERSE_ROW_ORDER_ANGLE = 0x93A4
del ctypes
del load_gl_proc
