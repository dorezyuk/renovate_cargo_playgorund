
trait Foo {
    fn bar<'a>(a: &Bar<'a>);
}

struct Bar<'b> {
    name: &'b str,
}

impl<'x, 'b> Foo for Bar<'b> {
    fn bar(a: &Bar<'x>)  {

    }
}

fn main() {}
