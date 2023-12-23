package com.letsbe.algorithms.util

import org.openjdk.jmh.annotations.Benchmark
import org.openjdk.jmh.annotations.BenchmarkMode
import org.openjdk.jmh.annotations.Mode
import org.openjdk.jmh.annotations.OutputTimeUnit
import org.openjdk.jmh.annotations.Scope
import org.openjdk.jmh.annotations.Setup
import org.openjdk.jmh.annotations.State
import org.openjdk.jmh.infra.Blackhole
import java.util.EnumMap
import java.util.concurrent.TimeUnit

@State(Scope.Thread)
class EnumMapBenchMark {
	private var enumMap: MutableMap<State, String>? = null
	private var hashMap: MutableMap<State, String>? = null

	@Setup
	fun setUp() {
		enumMap = EnumMap(State::class.java)
		hashMap = HashMap()
	}

	@Benchmark
	@BenchmarkMode(Mode.AverageTime)
	@OutputTimeUnit(TimeUnit.NANOSECONDS)
	fun enumMap(blackhole: Blackhole) {
		blackhole.consume(enumMap!!.put(State.SOLID, State.SOLID.name))
	}

	@Benchmark
	@BenchmarkMode(Mode.AverageTime)
	@OutputTimeUnit(TimeUnit.NANOSECONDS)
	fun hashMap(blackhole: Blackhole) {
		blackhole.consume(hashMap!!.put(State.SOLID, State.SOLID.name))
	}

	internal enum class State {
		SOLID,
		LIQUID,
		GAS
	}
}
