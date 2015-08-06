/* Complex.java */

public class Complex {

    public Complex() {

        this(0);
    }

    public Complex(int a) {

        this(a, 0);
    }

    public Complex(int a, int b) {
		//complex # = a + bi
        this.a = a;
        this.b = b;
    }

    public Complex add(Complex o) {
		// (a + bi) + (c+di) = (a+c) + (b+d)i
        return new Complex(a + o.a, b + o.b);
    }

    public Complex add(int n) {

        return new Complex(a + n, b);
    }

    public Complex div(Complex o) {
		
		Complex conj = (o.a, -o.b);
		int divisor = conjproduct(o);
		Complex num = mul(conj);
        return new Complex(num.a/divisor, num.b/divisor);
    }

    public Complex div(int n) {
		Complex den = new Complex(n);
        return div(den);
    }

    public Complex mul(Complex o) {
		//(a+bi)(c+di) = (ac - bd) + (ad + bc)i 
        return new Complex((a * o.a) - (b * o.b), (a * o.b) + (b * o.a));
    }

    public Complex mul(int n) {

        return new Complex(a * n, b * n);
    }
    
    public int conjproduct(Complex o) {
    	int conjugate = (o.a*o.a) + (o.b*o.b);
    	return conjugate ;
    }

    public Complex sub(Complex o) {
		// (a + bi) - (c+di) = (a-c) - (b-d)i
        return new Complex(a - o.a, b - o.b);
    }

    public Complex sub(int n) {

        return new Complex(a - n, b);
    }

    public String toString() {

        return "(" + a + " + " + b + "i " + ")";
    }

    private int a;
    private int b;
}
