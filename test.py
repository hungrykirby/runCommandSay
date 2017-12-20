def wait_key(timeout_sec):
    import signal

    __author__ = 'alfredplpl'

    def timeout(signum, frame):
        raise RuntimeError("timeout")

    signal.signal(signal.SIGALRM, timeout)
    signal.alarm(timeout_sec)
    try:
        key = input()
    except (RuntimeError):
        key = None
    finally:
        signal.alarm(0)

    return key


def take_test(q, a, tlimit=10):
    print(q)
    for i in range(tlimit):
        print(
            "\r制限時間{}秒 {}{} :".format(
                tlimit, '>' * (i + 1), '_' * (tlimit - i - 1)), end='')
        key = wait_key(1)
        if key is not None:
            if key == a:
                print('正解!')
                return True
            else:
                print('違うよ')
    print('時間切れ')
    return False


if __name__ == "__main__":
    take_test('もんだい. 10+20は?', '30')
