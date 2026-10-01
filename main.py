def read_scores(count: int) -> list[int]:
    scores = []
    while len(scores) < count:
        try:
            score = int(input(f"Введите оценку №{len(scores) + 1} (от 0 до 100): "))
            if 0 <= score <= 100:
                scores.append(score)
            else:
                print("Ошибка: оценка должна быть в диапазоне от 0 до 100.")
        except ValueError:
            print("Ошибка: требуется ввести целое число.")
    return scores


def show_statistics(scores: list[int]) -> None:
    if not scores:
        print("Нет результатов")
        return
    total = len(scores)
    total_sum = sum(scores)
    avg = round(total_sum / total, 2)
    passed = sum(1 for s in scores if s >= 70)
    print(
        f"Статистика: Среднее: {avg}; Мин: {min(scores)}; Макс: {max(scores)}; Прошли/Остальные: {passed}/{total - passed}"
    )


def retest_scores(scores: list[int]) -> list[int]:
    return sorted([score for score in scores if score < 70])


def replace_score(scores: list[int], number: int, value: int) -> bool:
    if not (1 <= number <= len(scores)) or not (0 <= value <= 100):
        return False
    scores[number - 1] = value
    return True


def main():
    print("=== Задание 4: Ввод 5 оценок ===")
    scores = read_scores(5)

    print("\n=== Задание 5: Статистика ===")
    show_statistics(scores)

    print("\n=== Задание 6: Список на пересдачу (< 70) ===")
    print("На пересдачу:", retest_scores(scores))

    print("\n=== Задание 7: Редактирование ===")
    while True:
        try:
            num = int(input(f"Введите номер оценки (1-{len(scores)}): "))
            val = int(input("Введите новую оценку (0-100): "))
            if replace_score(scores, num, val):
                print("Успешно изменено!")
                break
            print("Ошибка: неверный номер или значение вне диапазона!")
        except ValueError:
            print("Введите целые числа!")

    print("\n=== Обновлённые данные ===")
    show_statistics(scores)


if __name__ == "__main__":
    main()
