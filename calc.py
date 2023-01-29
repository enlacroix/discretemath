import streamlit as st
import numpy as np
from itertools import permutations

def tuple_to_str(tup):
    st = ''
    for u in list(tup):
        st += str(u)
    return st

def cycle_form(A):
    if A == '':
        return 0
    final = ''
    cycle_form = '('
    i = 0
    flag = True
    possible_i = list(range(len(A)))
    while flag:
        x = A[i]
        if x in cycle_form:
            cycle_form += ')'
            final += cycle_form
            cycle_form = '('
            if len(possible_i) == 0:
                pass
            else:
                i = possible_i[0]
            continue
        else:
            cycle_form += str(x)
            i = int(x) - 1
            if len(possible_i) == 0:
                pass
            else:
                possible_i.remove(i)
        cnt = sum([1 for s in final if s.isdigit()])
        if cnt == len(A):
            flag = False
    return final

def noc(a, b):
    i = min(a, b)
    while True:
        if i % a == 0 and i % b == 0:
            break
        i += 1
    return i

def multi_noc(A):
    list = A.copy()
    for i in range(0, len(list) - 1):
        list[i+1] = noc(list[i], list[i+1])
    return list[-1]

def multipy_permutation(A, B):
    result = ''
    if A == '' or B == '':
        return 'Один из множителей некорректен.'
    for i in range(1, len(A) + 1):
        result += str(B[int(A[i - 1]) - 1])
    return result

def cycle_class(s):
    x_list = cycle_form(s).replace(')', ' ').replace('(', ' ').split(' ')
    len_list = []
    N = len(x_list)
    for j in range(N):
        len_list.append(len(x_list[j]))
    len_2_list = []
    for x in len_list:
        if x > 1:
            len_2_list.append(x)
    if len(len_2_list) == 0:
        len_2_list.append(0)
    len_2_list.sort()
    return len_2_list

def deg_permutation(perm, n):
    result = perm
    for i in range(n - 1):
        result = multipy_permutation(result, perm)
    return result

def count_certain_cycle_structure(arr, n):  # подсчитает количество определенных цикловых структур до группы S9
    # print(count_certain_cycle_structure([2, 2, 2, 2], 8))
    cnt = 0
    x = list(range(1, n + 1))
    for s in list(permutations(x)):
        if tuple(cycle_class(tuple_to_str(s))) in set(permutations(arr)):
            cnt += 1
    return cnt

def find_inverse_perm(s):
    s = tuple_to_str(s)
    inv_s = ''
    neutral = tuple_to_str(tuple(range(1, len(s) + 1)))
    for sym in neutral:
        inv_s += str(s.find(sym) + 1)
    return inv_s

def gen_perm_matrix(s):
    n = len(s)
    A = np.zeros((n, n))
    for i in range(n):
        A[i][int(s[i]) - 1] = 1
    return A.astype(int)

def find_roots_of_perm(permutation, number):
    count = 0
    x = list(range(1, len(permutation) + 1))
    for s in list(permutations(x)):
        if deg_permutation(tuple_to_str(s), number) == tuple_to_str(permutation):
            st.sidebar.write(s, cycle_form(tuple_to_str(s)), beauty_list(cycle_class(tuple_to_str(s))))
            count += 1
    return count

def find_communicate_to_perm(permutation):
    count = 0
    x = list(range(1, len(permutation) + 1))
    for s in list(permutations(x)):
        if multipy_permutation(tuple_to_str(s), tuple_to_str(permutation)) == multipy_permutation(
                tuple_to_str(permutation), tuple_to_str(s)):
            count += 1
            st.sidebar.write(s, cycle_form(tuple_to_str(s)), beauty_list(cycle_class(tuple_to_str(s))))
    return count

def beauty_list(arr):
    return '(' + str(arr)[1:-1] + ')' + '-цикл'

def stack_sort(p):
    stack = [p[0]]
    answer = []
    for x in p[1:]:
        rev_stack = list(reversed(stack))
        if len(stack) > 0:
            for y in rev_stack:
                if y < x:
                    answer.append(y)
                    stack.remove(y)
                    if len(stack) == 0:
                        stack.append(x)
                else:
                    stack.append(x)
                    break
        else:
            stack.append(x)
    reve_stack = list(reversed(stack))
    answer += reve_stack
    return answer

def nod(a,b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b

def among_simple(a,b):
    if nod(a, b) == 1:
        return 1
    else:
        return 0




def eiler_function_straight(k):
    count = 0
    for i in range(1, k+ 1):
        if among_simple(i, k):
            count +=1
    return count

def eiler_function_reversed(k):
    count = 0
    a = []
    for j in range(1, 300+1):
        if eiler_function_straight(j) == k and count <= 5:
            a.append(j)
            count += 1
    return a
def inv_stack_sort(p):
    N = len(p)
    if N == 0:
        return ''
    p = list(p)
    arr = list(range(1, N + 1))
    for t in permutations(arr, N):
        if stack_sort(t) == p:
            return t
        else:
            continue
    st.write('Такую последовательность невозможно получить через стек! Если ты получил это сообщение, значит условие задачи некорректное.')
    return ''

def string_to_tuple(inp):
    sigma = []
    for i in inp:
        i = int(i)
        sigma.append(i)
    return tuple(sigma)

def list_to_str(arr):
    return ''.join(str(sym) for sym in arr)


def show_options(s, ind):
    invb = st.button('Найти обратную перестановку.', key=str(ind) + '1')
    if invb:
        st.sidebar.write('Обратная перестановка: ')
        st.sidebar.write(f"$ {s}^{{-1}} = {find_inverse_perm(s)}$")
    cycb = st.button('Цикловая форма и порядок.', key=str(ind) + '2')
    if cycb:
        st.sidebar.write('Цикловая запись')
        st.sidebar.write(f"$cycle = {cycle_form(s)}$")
        st.sidebar.write('Цикловый класс: ', beauty_list(cycle_class(s)))
        st.sidebar.write('Порядок: ', multi_noc(cycle_class(s)))
    mab = st.button('Вывести матрицу и определить четность.', key=str(ind) + '4')
    if mab:
        st.sidebar.dataframe(gen_perm_matrix(s))
        if np.linalg.det(gen_perm_matrix(s)) == 1:
            st.sidebar.write(s, ': чётная')
        else:
            st.sidebar.write(s, ': нечётная')
    n = st.number_input('Возвести в степень', 0, 20, value=0, key=str(ind) + '3')
    if n != 0:
        st.sidebar.write(f"$  {s}^{n} = {deg_permutation(s, n)}$")

st.sidebar.title('Панель вывода')



st.header('Калькулятор перестановок')
st.write('Добро пожаловать! Для вашего удобства мы ограничиваем перестановки до группы S9 включительно.')
st.subheader('1. Базовые операции.')
col1, col2 = st.columns(2)
with col1:
    a = st.text_area('Введите перестановку А: ', value = '24513')
    show_options(a, 1)
    # Все же сделать перестановку ООП классом? Или добавить латех-блок и фигурными скобками
with col2:
    b = st.text_area('Введите перестановку В: ', value = '34512')
    show_options(b, -1)
emp1, emp2, emp3 = st.columns(3)
with emp2:
    mpb = st.button('Перемножить А и В.')
    if mpb:
        st.sidebar.write('Результат композиции: ')
        st.sidebar.write(f"$a \circ b = {multipy_permutation(a, b)}$")
    impb = st.button('Перемножить B и A.')
    if impb:
        st.sidebar.write('Результат композиции: ')
        st.sidebar.write(f"$b \circ a = {multipy_permutation(b, a)}$")


st.subheader('2. Продвинутые расчёты.')
col4, col5, col6 = st.columns(3)
with col4:
    c = st.text_area('Введите цикловую структуру и группу перестановок.', value='2, 2, 3, 8')
    ch = st.checkbox('Вычислить')
    st.write('Пример: Найти число (2, 2, 3)-циклов в группе S8.')
    if ch:
        sub_arr = [int(x) for x in c.split(',')]
        st.write('Искомое количество: ', count_certain_cycle_structure(sub_arr[:-1], sub_arr[-1]))
with col5:
    d = st.text_area('Найти все квадратные корни из перестановки. ', value='251346')
    ch2 = st.checkbox('Вывести')
    if ch2:
        st.sidebar.write(find_roots_of_perm(d, 2))

with col6:
    e = st.text_area('Найти все перестановки x, коммутирующие с данной.', value='521436')
    ch3 = st.checkbox('Найти')
    if ch3:
        st.sidebar.write(find_communicate_to_perm(e))

st.subheader('3. Сортировка через стек')
f = st.text_area('Введите последовательность чисел.', value='1472635')
b1 = st.button('Сортировать через стек.')
if b1:
    st.write(list_to_str(stack_sort(f)))
b2 = st.button('Инвертировать через стек.') # (найти последовательность такую что, если ее отсортировать через стек, то получится исходная)
if b2:
    st.write(list_to_str(inv_stack_sort(f)))
b3 = st.button('Дважды инвертировать через стек.')
if b3:
    st.write(list_to_str(inv_stack_sort(inv_stack_sort(f))))
st.subheader('4. Функция Эйлера')
num = st.number_input('Введите число', 1, 1000, value=24)
eil1 = st.button('Найти функцию Эйлера')
if eil1:
    st.write(eiler_function_straight(num))
eil2 = st.button('Инвертировать функцию Эйлера') # на какие числа дали бы такое число, если найти от них фи Эйлера.
if eil2:
    st.sidebar.write(eiler_function_reversed(num))

