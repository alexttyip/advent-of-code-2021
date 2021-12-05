import java.io.File

fun main() {
    val lines = File("input.txt").readLines()
    val nums = lines.map { line -> line.trim().toInt(2) }

    val numBits = lines[0].length
    println(part1(nums, numBits))
    println(part2(nums, numBits))
}

fun part1(nums: List<Int>, numBits: Int): Int {
    var gamma = 0
    (0 until numBits).forEach { i ->
        val power = 1 shl i

        val count = nums.count {
            it and power > 0
        }

        if (nums.count() < count * 2) {
            gamma += power
        }
    }

    val epsilon = gamma xor ((1 shl numBits) - 1)

    return gamma * epsilon
}

fun List<Int>.getMoreOrLessCommon(power: Int, lessCommon: Boolean = false): List<Int> {
    if (count() <= 1)
        return this

    val (ones, zeros) = partition {
        it and power > 0
    }

    return if ((ones.count() >= zeros.count()) xor lessCommon) ones else zeros
}

fun part2(nums: List<Int>, numBits: Int): Int {
    var oxy = nums.toList()
    var co2 = nums.toList()

    (0 until numBits).reversed().forEach { i ->
        val power = 1 shl i

        oxy = oxy.getMoreOrLessCommon(power)
        co2 = co2.getMoreOrLessCommon(power, true)
    }

    return oxy.first() * co2.first()
}