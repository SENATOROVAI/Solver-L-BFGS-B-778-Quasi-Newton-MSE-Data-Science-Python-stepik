# FULL PYTHON SOLUTION

def main() -> None:
    g1, g2, s1, s2, y1, y2 = map(float, input().split())
    ys = y1 * s1 + y2 * s2
    rho = 1.0 / ys
    alpha = rho * (s1 * g1 + s2 * g2)
    q1 = g1 - alpha * y1
    q2 = g2 - alpha * y2
    gamma = ys / (y1 * y1 + y2 * y2)
    r1 = gamma * q1
    r2 = gamma * q2
    beta = rho * (y1 * r1 + y2 * r2)
    r1 = r1 + s1 * (alpha - beta)
    r2 = r2 + s2 * (alpha - beta)
    print(f"{-r1:.6f} {-r2:.6f}")


if __name__ == '__main__':
    main()
