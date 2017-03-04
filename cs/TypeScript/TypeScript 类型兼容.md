# TypeScript 类型兼容

## Simple

### Private & Protected

```typescript

/**
 * Created by simon on 2016/11/12.
 */
class Animal {
    private name;

    constructor(name: string) {
        this.name = name;
    }
}

class Dog extends Animal {
    constructor(name: string) {
        super(name)
    }
}

class Employee {
    protected name;

    constructor(name: string) {
        this.name = name
    }
}

const employee = new Employee("Simon Wang");
const dog = new Dog("Paul");
const animal: Animal = dog;
const animal2: Animal = employee; // error

```

编译不通过，Animal的name属性外界无法访问，所以导致Employee与Animal类型不兼容
> Error:(29, 7) TS2322: Type 'Employee' is not assignable to type 'Animal'.
 Property 'name' is private in type 'Animal' but not in type 'Employee'.


### protected & protected

```typescript

/**
 * Created by simon on 2016/11/12.
 */
class Animal {
    protected name;

    constructor(name: string) {
        this.name = name;
    }
}

class Dog extends Animal {
    constructor(name: string) {
        super(name)
    }
}

class Employee {
    protected name;

    constructor(name: string) {
        this.name = name
    }
}

const employee = new Employee("Simon Wang");
const dog = new Dog("Paul");
const animal: Animal = dog;
const animal2: Animal = employee; // error

```

> Error:(29, 7) TS2322: Type 'Employee' is not assignable to type 'Animal'.
Property 'name' is protected but type 'Employee' is not a class derived from 'Animal'.

### private & private

```typescript
/**
 * Created by simon on 2016/11/12.
 */
class Animal {
    private name;

    constructor(name: string) {
        this.name = name;
    }
}

class Dog extends Animal {
    constructor(name: string) {
        super(name)
    }
}

class Employee {
    private name;

    constructor(name: string) {
        this.name = name
    }
}

const employee = new Employee("Simon Wang");
const dog = new Dog("Paul");
const animal: Animal = dog;
const animal2: Animal = employee; // error

```
> Error:(29, 7) TS2322: Type 'Employee' is not assignable to type 'Animal'.
 Types have separate declarations of a private property 'name'.


### public & public

``` typescript

/**
 * Created by simon on 2016/11/12.
 */
class Animal {
    public name;

    constructor(name: string) {
        this.name = name;
    }
}

class Dog extends Animal {
    constructor(name: string) {
        super(name)
    }
}

class Employee {
    public name;

    constructor(name: string) {
        this.name = name
    }
}

const employee = new Employee("Simon Wang");
const dog = new Dog("Paul");
const animal: Animal = dog;
const animal2: Animal = employee;
```

> 编译通过
