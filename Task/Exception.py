print("1. SINGLE TRY WITH MULTIPLE EXCEPT")

try:
    num = int("abc")
    result = 100 / num

except ValueError:
    print("Invalid integer")

except ZeroDivisionError:
    print("Cannot divide by zero")

except Exception as e:
    print(e)


print("\n2. MULTIPLE TRY WITH SINGLE OUTER EXCEPT")

try:
    try:
        num = int("20")
    finally:
        print("First finally")

    try:
        result = 100 / 0
    finally:
        print("Second finally")

except ZeroDivisionError:
    print("Outer exception handled")


print("\n3. NESTED TRY WITH NESTED EXCEPT")

try:
    print("Outer try")

    try:
        num = int("abc")

    except ValueError:
        print("Inner except")

except Exception:
    print("Outer except")


print("\n4. NESTED TRY WITH NESTED EXCEPT AND FINALLY")

try:
    print("Outer try")

    try:
        num = int("abc")

    except ValueError:
        print("Inner except")

    finally:
        print("Inner finally")

except Exception:
    print("Outer except")

finally:
    print("Outer finally")


print("\n5. MULTIPLE TRY WITH MULTIPLE EXCEPT")

try:
    num = int("abc")

except ValueError:
    print("Invalid integer")

try:
    result = 100 / 0

except ZeroDivisionError:
    print("Cannot divide by zero")

try:
    my_list = [10, 20]
    print(my_list[5])

except IndexError:
    print("Invalid index")


print("\n6. MULTIPLE TRY WITH MULTIPLE EXCEPT AND FINALLY")

try:
    num = int("abc")

except ValueError:
    print("Invalid integer")

finally:
    print("First finally")

try:
    result = 100 / 0

except ZeroDivisionError:
    print("Cannot divide by zero")

finally:
    print("Second finally")

try:
    my_list = [10, 20]
    print(my_list[5])

except IndexError:
    print("Invalid index")

finally:
    print("Third finally")