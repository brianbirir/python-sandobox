class A:

    def do_this(self):

        print('do this in A')


class B(A):

    pass


class C:

    def do_this(self):

        print('do this in C')


class D(B, C):

    pass


d_instance = D()

d_instance.do_this()

print(D.mro()) # method resolution order
