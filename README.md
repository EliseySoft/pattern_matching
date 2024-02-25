# Pattern matching

## В репозитории находятся алгоритмы для эффективного соотнесения строк и шаблонов. 

## Структура:
1. [Непересекающиеся шаблоны](non_cross_patterns/) - алгоритм для мэтчинга непересекающихся шаблонов.
Каждый блок с переменными в шаблоне имеет начинается с xvx или xx, где x - переменная, v - подстрока.
2. [Шаблоны с одной переменной](one_var_patterns/) - шаблоны, в которых находится всего одна переменная.
3. [Регулярные шаблоны](regular_patterns/) - регулярные шаблоны. В них может находиться несколько переменных и при этом каждая переменная встречается всего один раз.
4. [Шаблоны с одной повторяющейся переменной](one_rep_var_patterns/) - шаблоны, в которых повторяется только одна переменная.
Все остальные переменные встречаются только по 1 разу.
5. [Шаблоны с k повторяющимися переменными](regular_patterns/) - шаблоны, в которых есть k повторяющихся переменных, а остальные переменные встречаются по 1 разу.
6. [Тестировочная система](testing_system/) - набор генераторов, каждый из которых умеет составлять строки и шаблоны по заданным параметрам.
